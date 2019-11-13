import pprint

paths = {
    '/bin/mkdir': None,
    'lib/init/vars/vars.sh': None,
    '/lib/init/vars.sh': None,
    '/home/documents/reports/report1.xls': None,
    '/home/music/album3/song2.mp3': None,
    '/home/music/album1/song2.mp3': None,
    '/lib/systemd/system/sudo.service': None
}

FILESYSTEM = {
    "/": [
        {
            'bin': [
                'echo',
                'mkdir',
                'ls',
                'ip',
                'kill'
            ]
        },
        {
            'lib': [
                {
                    'init': [
                        'fstab',
                        'vars.sh',
                        'upstart-job'
                    ]
                },
                {
                    'udev': [
                        'accelerometer',
                        'ata_id',
                        'cdrom_id'
                    ]
                },
                {
                    'systemd': [
                        {
                            'system': [
                                'sudo.service',
                                'rsync.service',
                                'anacron.service'
                            ]
                        },
                        {
                            'system-sleep': [
                                'notify-upower.sh'
                            ]
                        },
                        'systemd-logind',
                        'systemd-udevd',
                        'systemd-localed'
                    ]
                }
            ]
        },
        {
            'home': [
                {
                    'documents': [
                        {
                            'reports': []
                        },
                        'ToDo.txt',
                        'book.pdf',
                        'results.pdf'
                    ]
                },
                {
                    'music': [
                        {
                            'album1': [
                                'song1.mp3',
                                'song2.mp3'
                            ]
                        },
                        {
                            'album2': [
                                'song1,mp3',
                                'song2.mp3'
                            ]
                        }
                    ]
                },
                {
                    'pictures': [
                        {
                            'holiday': [
                                'photo1.jpg',
                                'photo2.jpg',
                                'photo3.jpg',
                                'photo4.jpg'
                            ]
                        },
                        {
                            'trip': [
                                'photo1.jpg',
                                'photo2.jpg',
                                'photo3.jpg',
                                'photo4.jpg'
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}


def search_directory(directory, path):
    for subpath in directory:
        if isinstance(subpath, dict):
            if path in subpath:
                return subpath[path]
        if isinstance(subpath, str):
            if subpath == path:
                return path
    return None


def file_exists(path):
    cwd = FILESYSTEM
    parts = path.split('/')
    for index, part in enumerate(parts):
        if not part:
            cwd = cwd['/']
            continue
        subdirectory_or_file = search_directory(cwd, part)
        if isinstance(subdirectory_or_file, list):
            cwd = subdirectory_or_file
        elif isinstance(subdirectory_or_file, str):
            if index == len(parts) - 1:
                return True
            else:
                # we reached file in FILESYSTEM but in a path this a directory
                return False
        else:
            return False
    return True


def main():
    for path in paths:
        paths[path] = file_exists(path)
    pprint.pprint(paths)


main()
