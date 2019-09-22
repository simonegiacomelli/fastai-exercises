import random
import tarfile

import numpy as np
from PIL import Image, ImageDraw

from core import folders, delete_folder_recursively


def archive(archive_name):
    archive_path = folders.data / (archive_name + '.tgz')
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(folders.data / archive_name, arcname=archive_name)
    print(f'generated archive {str(archive_path)}')


def generate_class(archive_name, class_name, class_gen):
    sets = [('train', 300), ('valid', 60), ('test', 30)]
    for set_name, _ in sets:
        delete_folder_recursively(folders.data / archive_name / set_name / class_name)

    def generate_set(set_name, n):
        f = folders.data / archive_name / set_name / class_name
        f.mkdir(parents=True, exist_ok=True)

        for i in range(1, n + 1):
            print(str(f), i)
            im = class_gen()
            im.save(f / f'{i}.png')

    for set_name, n in sets:
        generate_set(set_name, n)


def mktr(x, y):
    return np.array([[1, 0, x],
                     [0, 1, y],
                     [0, 0, 1]])


def mkrot(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])


def random_color():
    return tuple([random.randint(0, 255) for _ in range(3)])


def apply_pt(f, point2d):
    p3d = np.array([[point2d[0], point2d[1], 1]]).T
    t = f @ p3d
    p = (t[0][0], t[1][0])
    return p


def apply_pts(f, points2d):
    return [apply_pt(f, p2d) for p2d in points2d]


def new_rect(res, w, h, transform, angle, bk_col=None, fg_col=None):
    if not bk_col: bk_col = random_color()
    if not fg_col: fg_col = random_color()
    w2 = w // 2
    h2 = h // 2
    p1 = (-w2, -h2)
    p2 = (-w2, h2)
    p3 = (w2, h2)
    p4 = (w2, -h2)

    original_rectangle = [p1, p2, p3, p4, p1]

    tr = transform @ mkrot(np.deg2rad(angle))
    points = apply_pts(tr, original_rectangle)

    im = Image.new("RGB", res, bk_col)
    dr = ImageDraw.Draw(im)

    width = 10
    w2 = (width - 2) / 2
    dr.line(points, fill=fg_col, width=width)
    for (x, y) in points:
        dr.ellipse((x - w2, y - w2, x + w2, y + w2), fill=fg_col)
    return im


def new_tri(res, p1, p2, p3, transform, angle, bk_col=None, fg_col=None):
    if not bk_col: bk_col = random_color()
    if not fg_col: fg_col = random_color()

    original_triangle = [p1, p2, p3, p1]

    tr = transform @ mkrot(np.deg2rad(angle))
    points = apply_pts(tr, original_triangle)

    im = Image.new("RGB", res, bk_col)
    dr = ImageDraw.Draw(im)

    width = 10
    w2 = (width - 2) / 2
    dr.line(points, fill=fg_col, width=width)
    for (x, y) in points:
        dr.ellipse((x - w2, y - w2, x + w2, y + w2), fill=fg_col)
    return im
