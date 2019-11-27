import os
import sys


def print_match(match):
    file_type = 'FILE' if os.path.isfile(match) else 'DIR'
    print(f'{file_type} : {match}')


def search(path, pattern):
    for subpath in os.listdir(path):
        absolute_subpath = os.path.join(path, subpath)
        if pattern in subpath:
            print_match(absolute_subpath)
        if os.path.isdir(absolute_subpath):
            search(absolute_subpath, pattern)


if __name__ == '__main__':
    try:
        path, pattern = sys.argv[1:]
    except ValueError:
        print('The script needs exactly two command line arguments!')
    else:
        search(path, pattern)
