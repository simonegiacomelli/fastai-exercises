import random

from lesson1.dataset import random_color, new_rect, new_tri, mktr, archive
from lesson1.dataset import generate_class
import numpy as np
from random import randint as ri


def random_rect():
    iw = 640
    ih = 480
    w = random.randint(30, 140)
    h = random.randint(30, 140)
    tx = random.randint(w, iw - w)
    ty = random.randint(w, ih - w)
    angle = random.randint(0, 180)
    transform = mktr(tx, ty)
    return new_rect((iw, ih), w, h, transform, angle)


def random_tri():
    iw = 640
    ih = 480
    mi = 15
    ma = 50
    p1 = ri(-ma, -mi), ri(mi, ma)
    p2 = ri(mi, ma), ri(mi, ma)
    p3 = ri(-mi, mi), ri(-ma, -mi)

    w = int(np.sqrt(2) * ma * 2)
    tx = ri(w, iw - w)
    ty = ri(w, ih - w)
    angle = ri(0, 360)
    transform = mktr(tx, ty)

    return new_tri((iw, ih), p1, p2, p3, transform, angle)


def generate():
    generate_class('tri_and_rect2', 'tri', random_tri)
    generate_class('tri_and_rect2', 'rect', random_rect)
    archive('tri_and_rect2')


if __name__ == '__main__':
    generate()
