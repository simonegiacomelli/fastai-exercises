import random
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


def mktr(x, y):
    return np.array([[1, 0, x],
                     [0, 1, y],
                     [0, 0, 1]])


def mkrot(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])


def apply_pt(f, point2d):
    p3d = np.array([[point2d[0], point2d[1], 1]]).T
    t = f @ p3d
    p = (t[0][0], t[1][0])
    return p


def apply_pts(f, points2d):
    return [apply_pt(f, p2d) for p2d in points2d]


def new_tri(res, w, tr, angle, bk_col, fg_col):
    h = w / 2 * np.sqrt(3)
    p1 = (-w / 2, h / 2)
    p2 = (w / 2, h / 2)
    p3 = (0, -h / 2)

    original_triangle = [p1, p2, p3, p1]

    tr = mktr(*tr) @ mkrot(np.deg2rad(angle))
    points = apply_pts(tr, original_triangle)

    im = Image.new("RGB", res, bk_col)
    dr = ImageDraw.Draw(im)

    width = 10
    w2 = (width - 2) / 2
    dr.line(points, fill=fg_col, width=width)
    for (x, y) in points:
        dr.ellipse((x - w2, y - w2, x + w2, y + w2), fill=fg_col)
    return im


def basic_tri():
    res = 640, 480
    w = 140
    tr = 300, 100
    angle = 90
    bk_col = (255, 255, 255)
    fg_col = (255, 50, 50)
    return res, w, tr, angle, bk_col, fg_col


def random_color():
    return tuple([random.randint(0, 255) for _ in range(3)])


def random_tri():
    iw = 640
    ih = 480
    w = random.randint(30, 140)
    tx = random.randint(w, iw - w)
    ty = random.randint(w, ih - w)
    angle = random.randint(0, 120)
    bk_col = random_color()
    fg_col = random_color()
    return (iw, ih), w, (tx, ty), angle, bk_col, fg_col


random.seed(42)


def create_triangle_folder(folder, n):
    f = Path(folder)
    f.mkdir(parents=True, exist_ok=True)

    for i in range(1, n + 1):
        print(folder, i)
        im = new_tri(*(random_tri()))
        im.save(f.joinpath(f'{i}.png'))


create_triangle_folder('tri_and_rect/train/tri', n=3000)
create_triangle_folder('tri_and_rect/valid/tri', n=600)
create_triangle_folder('tri_and_rect/test/tri', n=300)
