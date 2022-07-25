from argparse import ArgumentParser
import sys
import glob
import asyncio

def create_executable_for_method(program_name, method_name):
    async def executable(parsed_args):
        cmd = ['/bin/bash', program_name, f'{parsed_args.output_prefix}_{method_name}.csv', f"{' '.join(parsed_args.datasets)}"]
        process = await asyncio.create_subprocess_exec(*cmd)
        await process.wait()
        return process.returncode, method_name

    return executable

def get_fs_methods():
    program_names = glob.glob('methods/*/run.sh')
    fs_methods = {}
    for program_name in program_names:
        method_name = program_name.split('/')[1].lower()
        fs_methods[method_name] = create_executable_for_method(program_name, method_name)
    return fs_methods

ml_models = ['svm', 'rf']
fs_methods = get_fs_methods()

def parse_args():
    parser = ArgumentParser(description="Suite to run feature selection (FS) methods and evaluation of machine learning (ML) algorithms")
    subparsers = parser.add_subparsers(title='Available commands', dest="command")

    list_parser = subparsers.add_parser('list', help='List available feature selection methods and/or machine learning models')
    list_group = list_parser.add_mutually_exclusive_group(required=True)
    list_group.add_argument("--all", action='store_true')
    list_group.add_argument("--fs-methods", action='store_true')
    list_group.add_argument("--ml-models", action='store_true')

    run_parser = subparsers.add_parser("run", help='Run experiment with feature selection methods and ML models')
    run_parser.add_argument(f'--fs-methods', help=f'Feature selection methods to include', choices=list(fs_methods.keys()) + ['all'], nargs='*', default='all')
    run_parser.add_argument(f'--ml-models', help=f'Machine learning models to include', choices=ml_models + ['all'], nargs='*', default='all')
    run_parser.add_argument('-d', '--datasets', required=True, help='Datasets to run the experiment', nargs='+')
    run_parser.add_argument('--output-prefix', help='Output file prefix. Default: result', default='result')

    args = parser.parse_args(sys.argv[1:])
    return args

async def run_command(parsed_args):
    chosen_methods = list(fs_methods.keys()) if 'all' in parsed_args.fs_methods else parsed_args.fs_methods
    tasks = []
    for method in chosen_methods:
        print(f"STARTING {method}")
        tasks.append(asyncio.create_task(fs_methods[method](parsed_args)))

    for task in tasks:
        await task
    
    for task in tasks:
        returncode, method_name = task.result()
        if(returncode == 0):
            print(f'FINISHED SUCCESSFULLY {method_name}')

def list_command(parsed_args):
    if(parsed_args.fs_methods):
        print(', '.join(fs_methods))
    elif(parsed_args.ml_models):
        print(', '.join(ml_models))
    else:
        print('methods:', ', '.join(fs_methods.keys()))
        print('models:', ', '.join(ml_models))

command = {
    'run' : lambda parsed_args: asyncio.run(run_command(parsed_args)),
    'list': list_command
}

def main():
    parsed_args = parse_args()
    if(parsed_args.command == None):
        print("Error: you must use one of these commands:", ', '.join(command.keys()))
        exit(1)
    command[parsed_args.command](parsed_args)
        
if __name__ == '__main__':
    main()
