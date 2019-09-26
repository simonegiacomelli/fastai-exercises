from functools import partial

from PIL import Image, ImageDraw
import numpy as np
from lesson1.dataset import apply_pt, mktr, mkrot

import matplotlib.pyplot as plt


def annotate_pts(ax, args):
    for arg in args:
        annotate(ax, *args)


def annotate(ax, txt, pt, color='red', suffix='', tr=None):
    if tr is not None:
        pt = apply_pt(tr, pt)
    x = pt[0]
    y = pt[1]
    ax.scatter(x, y, color=color)

    ax.annotate(txt + suffix + f' {np.round(x, 2)},{np.round(y, 2)}', apply_pt(mktr(0.04, 0.03), pt))


class Rot1:
    def __init__(self):
        fig, (self.left, self.right) = plt.subplots(ncols=2)
        self.left.grid(True, which='both')
        self.right.grid(True, which='both')
        self.left.axis('equal')
        self.right.axis('equal')

    def calc(self, a, b, p):
        annotate(self.left, 'a', a)
        annotate(self.left, 'b', b)
        annotate(self.left, 'p', p)

        subtract = np.subtract(b, a)[::-1]
        print(subtract)
        alpha = np.arctan2(*subtract)
        print(alpha)
        # alpha = np.deg2rad(90)
        # print(alpha)
        tr = mkrot(-alpha) @ mktr(-a[0], -a[1])
        an2 = partial(annotate, self.right, color='green', tr=tr)
        an2('a', a)
        an2('b', b)
        an2('p', p)

    def calc2(self, a, b, p):
        annotate(self.left, 'a', a)

        alpha = np.deg2rad(90)
        tr = mkrot(alpha)
        an2 = partial(annotate, self.right, color='green', tr=tr)
        an2('a', a)


# Rot1().calc2((3, -1), (3, -4), (1, -2))
Rot1().calc((3, -1), (3, -4), (1, -2))
plt.show()
