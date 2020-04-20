import os
import shutil

import magic


def remove_folder(path):
    shutil.rmtree(path, ignore_errors=True)


def is_video(path):
    return False if not file_exist(path) else 'video' in magic.from_file(path, mime=True)


def file_exist(path):
    return os.path.exists(path)


def add_prefix_to_filename(path, prefix):
    file_path, filename_with_extension = os.path.split(path)
    return os.path.join(file_path, f'{prefix}{filename_with_extension}')


def replace_extension(path, extension):
    file_path, filename_with_extension = os.path.split(path)
    filename = os.path.splitext(filename_with_extension)[0]
    return os.path.join(file_path, f'{filename}{extension}')
