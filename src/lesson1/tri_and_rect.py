import random

from lesson1.dataset import random_color, new_rect, new_tri, mktr, archive
from lesson1.dataset import generate_class
import numpy as np


def random_rect():
    iw = 640
    ih = 480
    w = random.randint(30, 140)
    h = random.randint(30, 140)
    tx = random.randint(w, iw - w)
    ty = random.randint(w, ih - w)
    angle = random.randint(0, 180)
    bk_col = random_color()
    fg_col = random_color()
    transform = mktr(tx, ty)
    return new_rect((iw, ih), w, h, transform, angle, bk_col, fg_col)


def random_tri():
    iw = 640
    ih = 480
    w = random.randint(30, 140)
    tx = random.randint(w, iw - w)
    ty = random.randint(w, ih - w)
    angle = random.randint(0, 120)
    transform = mktr(tx, ty)
    h = w / 2 * np.sqrt(3)
    p1 = (-w / 2, h / 2)
    p2 = (w / 2, h / 2)
    p3 = (0, -h / 2)
    return new_tri((iw, ih), p1, p2, p3, transform, angle)

if __name__ == '__main__':
    generate_class('tri_and_rect', random_tri, random_rect)
