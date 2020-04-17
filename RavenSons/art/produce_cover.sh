#!/bin/bash
./generate_cover.py
convert raven_sons.png -crop 2160x2160+621+618 raven_sons.png
geeqie