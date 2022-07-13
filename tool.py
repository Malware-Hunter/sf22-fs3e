from argparse import ArgumentParser
import sys
import glob
import os
from methods.utils import get_base_parser, get_dataset, get_X_y

fs_methods = [dir.replace('./methods/', '').lower() for dir in glob.glob('./methods/[a-zA-Z]*') if os.path.isdir(dir)]
ml_models = ['svm', 'rf']

def parse_args():
    base_parser = get_base_parser()
    parser = ArgumentParser(description="Suite to run feature selection (FS) methods and evaluation of machine learning (ML) algorithms")
    subparsers = parser.add_subparsers(title='Available commands', dest="command")

    list_parser = subparsers.add_parser('list', help='List available feature selection methods and/or machine learning models')
    list_group = list_parser.add_mutually_exclusive_group(required=True)
    list_group.add_argument("--all", action='store_true')
    list_group.add_argument("--fs-methods", action='store_true')
    list_group.add_argument("--ml-models", action='store_true')

    run_parser = subparsers.add_parser("run", parents=[base_parser], help='Run experiment with feature selection methods and ML models')
    run_parser.add_argument(f'--fs-methods', help=f'Feature selection methods to include', choices=fs_methods + ['all'], nargs='*', default='all')
    run_parser.add_argument(f'--ml-models', help=f'Machine learning models to include', choices=ml_models + ['all'], nargs='*', default='all')

    args = parser.parse_args(sys.argv[1:])
    return args

def run_command(parsed_args):
    print(parsed_args)
    X, y = get_X_y(parsed_args, get_dataset(parsed_args))

def list_command(parsed_args):
    if(parsed_args.fs_methods):
        print(', '.join(fs_methods))
    elif(parsed_args.ml_models):
        print(', '.join(ml_models))
    else:
        print('methods:', ', '.join(fs_methods))
        print('models:', ', '.join(ml_models))

command = {
    'run' : run_command,
    'list': list_command
}

def main():
    parsed_args = parse_args()
    command[parsed_args.command](parsed_args)
        
if __name__ == '__main__':
    main()
