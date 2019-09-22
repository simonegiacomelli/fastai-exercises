import os
import pathlib


class Folders:
    def __init__(self, name):
        self._core_folder = os.path.dirname(__file__)

        self._core = pathlib.Path(self._core_folder).resolve()
        self._root = self._core.joinpath('../..').resolve()
        self.data = self._root.joinpath(name).absolute()
