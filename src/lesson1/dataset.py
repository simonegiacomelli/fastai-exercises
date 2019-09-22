import random
import tarfile

import numpy as np
from PIL import Image, ImageDraw

from core import folders, delete_folder_recursively


def archive(name):
    with tarfile.open(folders / (name + '.tgz'), "w:gz") as tar:
        tar.add(folders / name, arcname=name)


def generate(name, tri, rect):
    delete_folder_recursively(folders.data / name)

    def generate_class(class_name, gen):
        def generate_set(set_name, n):
            f = folders.data / name / set_name / class_name
            f.mkdir(parents=True, exist_ok=True)

            for i in range(1, n + 1):
                print(str(f), i)
                im = gen()
                im.save(f / f'{i}.png')

        generate_set('train', 300)
        generate_set('valid', 60)
        generate_set('test', 30)

    generate_class('tri', tri)
    generate_class('rect', rect)


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


def new_rect(res, w, h, tr, angle, bk_col, fg_col):
    w2 = w // 2
    h2 = h // 2
    p1 = (-w2, -h2)
    p2 = (-w2, h2)
    p3 = (w2, h2)
    p4 = (w2, -h2)

    original_rectangle = [p1, p2, p3, p4, p1]

    tr = mktr(*tr) @ mkrot(np.deg2rad(angle))
    points = apply_pts(tr, original_rectangle)

    im = Image.new("RGB", res, bk_col)
    dr = ImageDraw.Draw(im)

    width = 10
    w2 = (width - 2) / 2
    dr.line(points, fill=fg_col, width=width)
    for (x, y) in points:
        dr.ellipse((x - w2, y - w2, x + w2, y + w2), fill=fg_col)
    return im


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