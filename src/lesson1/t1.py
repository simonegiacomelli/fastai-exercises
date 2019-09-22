import core


from core import folders
from fastai.vision import *
from fastai.metrics import error_rate

print(folders.data)
print(folders.data/'ciao')
folders.data.ls()
help(ImageDataBunch.from_folder)
help(Path.ls)
