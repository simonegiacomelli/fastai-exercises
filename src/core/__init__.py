import os
import shutil
import time
from pathlib import Path
from typing import Union

from core.folders import Folders

folders = Folders('data')

PathOrStr = Union[Path, str]


def delete_folder_recursively(path: PathOrStr):
    path = str(path)
    if not os.path.exists(path):
        return
    assert os.path.isdir(path), path
    print(f'Removing [{path}]')
    shutil.rmtree(path, ignore_errors=True)

    # sometimes rmtree fails to remove files
    for tries in range(20):
        if os.path.exists(path):
            print(f'path still exist! {path}')
            time.sleep(0.1)
            shutil.rmtree(path, ignore_errors=True)

    if os.path.exists(path):
        shutil.rmtree(path)

    if os.path.exists(path):
        raise Exception(f'Unable to remove folder [{path}]')
