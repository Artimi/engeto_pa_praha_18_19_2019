import os.path
import shutil
import sys

IMAGES = 'Images'
DOCS = 'Docs'
TABLES = 'Tables'
PRESENTATIONS = 'Presentations'

FORMATS = {
    'png': IMAGES,
    'jpg': IMAGES,
    'jpeg': IMAGES,
    'tiff': IMAGES,
    'gif': IMAGES,
    'doc': DOCS,
    'docx': DOCS,
    'odt': DOCS,
    'txt': DOCS,
    'pdf': DOCS,
    'xls': TABLES,
    'xlsx': TABLES,
    'ppt': PRESENTATIONS,
    'pptx': PRESENTATIONS
}


def move(path, dir):
    os.makedirs(dir, exist_ok=True)
    file_name = os.path.basename(path)
    # shutil.move(path, os.path.join(dir, file_name))
    print(f'Moved file {path} to directory {dir}')


def cleanup(path):
    for subpath in os.listdir(path):
        absolute_subpath = os.path.join(path, subpath)
        if os.path.isfile(absolute_subpath):
            try:
                extension = subpath.split('.', maxsplit=1)[1]
            except IndexError:
                continue

            try:
                move(absolute_subpath, FORMATS[extension])
            except KeyError:
                continue


if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except ValueError:
        print('The script demands one argument!')
        exit(1)
    if not os.path.isdir(path):
        print(f'The given path = {path} is not a directory!')
        exit(1)

    cleanup(path)
