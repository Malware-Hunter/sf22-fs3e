from argparse import ArgumentParser
import sys
from methods.utils import get_base_parser, get_dataset, get_X_y


def parse_args():
    base_parser = get_base_parser()
    parser = ArgumentParser(description="Suite de métodos de seleção de características e de validação com algoritmos de Machine Learning")
    subparsers = parser.add_subparsers(title='Comandos disponíveis')

    list_command = subparsers.add_parser('list')
    # Adicionar opções mutuamente exclusivas para listar métodos, modelos ou todos

    run_command = subparsers.add_parser("run", parents=[base_parser])
    # Adicionar outras opções do run aqui

    args = parser.parse_args(sys.argv[1:])
    return args


def main():
    parsed_args = parse_args()
    X, y = get_X_y(parsed_args, get_dataset(parsed_args))
    print(X, y)
    print(parsed_args)


if __name__ == '__main__':
    main()
