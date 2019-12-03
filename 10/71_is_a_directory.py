
import os.path


def which(path):
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'dir'
    return None


print(which('71_is_a_directory.py'))
print(which('70_import_hacks/'))
print(which('nonexistent.file'))
