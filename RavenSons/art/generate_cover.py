#!/usr/bin/python3
"""Generate cover art for Graviteka - Raven Sons"""
__author__ = "Andrey Zamaraev (a5kin)"

import random
import math

import numpy as np

from probart.canvas import EntropyCanvas  # pip3 install probart

CANVAS_WIDTH, CANVAS_HEIGHT = 1666 * 2, 1666 * 2
LINE_WIDTH = 2

# background parameters
NUM_LINES = 6666 * 5
NUM_SHADES = 2
NUM_CLONES = 1

BACKGROUND_COLOR = (0, 0, 0)
COLOR1 = (0.5, 0, 0.7, 0.1)
COLOR2 = (1, 0.7, 0, 0.1)

RADIUS = 0.3

DEV = 0.01
SUBDEV = 0.008

# eye parameters
NUM_CLONES1 = NUM_CLONES2 = 13

FULL_COLOR1 = (0.7, 0, 1, 0.1)
FULL_COLOR2 = (1, 1, 1, 0.1)
EMPTY_COLOR1 = EMPTY_COLOR2 = (0, 0, 0, 0.1)

RADIUS1 = 0.23
RADIUS2 = RADIUS1 * 0.8

random.seed("Raven Sons9")

MU1 = MU2 = random.random()
MU2 = random.random() * 0 + MU1
SIGMA1 = random.random()
SIGMA2 = random.random() * 0 + 0.2

DEV1 = 0.01
SUBDEV1 = 0.001
DEV2 = 0.005
SUBDEV2 = 0.001
NUM_POINTS1 = NUM_POINTS2 = 666

# logo path
GRAVITEKA_LOGO = [
    [(41, 34), (41, 18), (47, 12), (53, 18), (47, 24), (53, 30), (53, 34)],
    [(31, 24), (37, 24), (37, 34), (24, 34), (21, 31), (21, 25), (34, 12), (41, 12), (38, 15)],
    [(72, 12), (53, 12), (66, 25), (66, 34)],
    [(62, 31), (61, 31), (57, 35), (57, 22), (59, 20)],
    [(70, 27), (70, 29), (76, 35), (76, 12)],
    [(83, 34), (83, 24)],
    [(83, 20), (83, 19)],
    [(80, 12), (100, 12), (97, 15)],
    [(111, 31), (111, 32), (111, 34), (100, 34), (97, 31), (97, 21), (106, 12), (111, 17), (111, 18)],
    [(90, 16), (90, 34)],
    [(113, 12), (112, 12), (116, 16), (116, 34)],
    [(125, 18), (119, 24), (125, 30), (125, 34)],
    [(131, 20), (129, 22), (129, 35), (133, 31), (134, 31)],
    [(138, 34), (138, 25), (125, 12), (118, 12), (116, 10)],
    [(106, 24), (99, 24)]
]

# title path
RAVEN_SONS = [
    [(15, 17), (15, 9), (18, 9), (20, 11), (18, 13), (16, 13), (20, 17)],
    [(22, 17), (22, 12), (25, 9), (27, 11), (27, 17), (23, 13)],
    [(29, 9), (29, 15), (31, 17), (34, 14), (34, 9)],
    [(41, 17), (38, 17), (36, 15), (36, 12), (39, 9), (41, 11), (41, 13), (37, 13)],
    [(43, 17), (43, 9), (45, 9), (48, 12), (48, 17)],
    [(55, 17), (58, 17), (60, 15), (60, 13), (55, 13), (55, 11), (57, 9), (60, 9)],
    [(62, 11), (62, 15), (64, 17), (65, 17), (67, 15), (67, 11), (65, 9), (64, 9), (62, 11)],
    [(69, 17), (69, 9), (71, 9), (74, 12), (74, 17)],
    [(76, 17), (79, 17), (81, 15), (81, 13), (76, 13), (76, 11), (78, 9), (81, 9)]
]

random.seed("Breed Of Satan666")


def generate_path(r, mu, sigma, num_points, form=0):
    """Generate circular path."""
    angles = [0] + [random.gauss(mu, sigma) * math.pi for _ in range(num_points)]
    angles += [2 * math.pi - a for a in angles[::-1]]
    if form:
        points = [(0.5 * r * math.sin(fi) ** 3 + 0.5, r * math.cos(fi) + 0.5) for fi in angles]
    else:
        points = [(r * math.sin(fi) + 0.5, r * math.cos(fi) + 0.5) for fi in angles]
    path = points + [points[0]]
    return path


def main():
    canvas = EntropyCanvas(CANVAS_WIDTH, CANVAS_HEIGHT, BACKGROUND_COLOR)
    line_width = LINE_WIDTH / CANVAS_WIDTH

    # background
    colors = np.linspace(COLOR1, COLOR2, NUM_SHADES).tolist()
    for i in range(NUM_LINES):
        x1, x2 = 0.5 - RADIUS, 0.5 + RADIUS
        y1 = y2 = 0.5 + (2 * i / NUM_LINES - 1) * RADIUS
        dev = 0.1
        y1 = max(0.5 - RADIUS, min(0.5 + RADIUS, y1 + RADIUS * (random.random() * dev - dev / 2)))
        y2 = max(0.5 - RADIUS, min(0.5 + RADIUS, y2 + RADIUS * (random.random() * dev - dev / 2)))
        color_pos = int((i + (random.gauss(0.5, 0.5) - 0.5) * (NUM_LINES - 1)) * NUM_SHADES / NUM_LINES)
        color = colors[max(0, min(NUM_SHADES - 1, color_pos))]
        path = [(x1, y1), (x2, y2)]
        canvas.multiline(path, color, color, NUM_CLONES, line_width, DEV, SUBDEV)

    # eye contour
    path = generate_path(RADIUS1, MU1, SIGMA1, NUM_POINTS1, form=1)
    path = [(y, x) for x, y in path]
    canvas.multiline(path, FULL_COLOR1, FULL_COLOR2, NUM_CLONES1,
                     line_width, DEV1, SUBDEV1)
    for i in range(13):
        path = generate_path(RADIUS2 * (0.8 ** i), MU2 * (0.9 ** i),
                             SIGMA2, int(NUM_POINTS2 * (0.8 ** i)), form=1)
        path = [(y, x) for x, y in path]
        canvas.multiline(path, EMPTY_COLOR1, EMPTY_COLOR2, NUM_CLONES2,
                         line_width, DEV2, SUBDEV2)

    # eyeball
    path = generate_path(RADIUS1 * 0.32, MU1, SIGMA1, NUM_POINTS1)
    path = [(y, x) for x, y in path]
    canvas.multiline(path, COLOR1, FULL_COLOR2, NUM_CLONES1,
                     line_width, DEV1, SUBDEV1)
    for i in range(5):
        path = generate_path(RADIUS2 * 0.23 * (0.8 ** i), MU2 * (0.8 ** i),
                             SIGMA2 * 1.01, int(NUM_POINTS2 * (0.8 ** i)))
        path = [(1 - y, x) for x, y in path]
        canvas.multiline(path, EMPTY_COLOR1, EMPTY_COLOR2, NUM_CLONES2,
                         line_width, DEV2, SUBDEV2)

    # band's logo
    for path in GRAVITEKA_LOGO:
        path = [(x / 270 + 0.21, y / 270 + 0.2) for x, y in path]
        canvas.multiline(path, EMPTY_COLOR1, EMPTY_COLOR2, 184,
                         line_width, DEV2 * 2, SUBDEV2)

    for path in GRAVITEKA_LOGO:
        path = [(x / 270 + 0.21, y / 270 + 0.2) for x, y in path]
        canvas.multiline(path, COLOR1, COLOR2, 184,
                         line_width, DEV2 * 1.3, SUBDEV2)

    # album's title
    for path in RAVEN_SONS:
        path = [(x / 420 + 0.39, y / 420 + 0.68) for x, y in path]
        canvas.multiline(path, EMPTY_COLOR1, EMPTY_COLOR2, 32,
                         line_width, DEV2 / 1.8, SUBDEV2 / 2)

    for path in RAVEN_SONS:
        path = [(x / 420 + 0.39, y / 420 + 0.68) for x, y in path]
        canvas.multiline(path, COLOR2, COLOR1, 32,
                         line_width, DEV2 / 2, SUBDEV2 / 2)

    canvas.save_to("raven_sons.png")


if __name__ == "__main__":
    main()
