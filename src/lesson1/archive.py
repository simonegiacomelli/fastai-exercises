import tarfile

from core import folders


def create(name):
    with tarfile.open(folders / (name + '.tgz'), "w:gz") as tar:
        tar.add(folders / name, arcname=name)
