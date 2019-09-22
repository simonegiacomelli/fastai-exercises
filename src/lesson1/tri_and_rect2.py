import random

from lesson1.dataset import random_color, new_rect, new_tri
from lesson1.dataset import generate


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
    return new_rect((iw, ih), w, h, (tx, ty), angle, bk_col, fg_col)


def random_tri():
    iw = 640
    ih = 480
    w = random.randint(30, 140)
    tx = random.randint(w, iw - w)
    ty = random.randint(w, ih - w)
    angle = random.randint(0, 120)
    bk_col = random_color()
    fg_col = random_color()
    return new_tri((iw, ih), w, (tx, ty), angle, bk_col, fg_col)


if __name__ == '__main__':
    generate('tri_and_rect2', random_tri, random_rect)