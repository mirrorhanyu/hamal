import shutil


def remove_folder(path):
    shutil.rmtree(path, ignore_errors=True)

