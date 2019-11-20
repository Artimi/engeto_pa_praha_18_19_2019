def file_loader(path):
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError:
        print(f'File {path} does not exist.')
        return None



print(file_loader('nonexistent'))
print('-' * 80)
print(file_loader('59_file_loader.py'))
