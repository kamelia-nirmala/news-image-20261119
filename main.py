#!/usr/bin/env python3
"""Write the 19 Nov 2026 world-news summary image to /output/entry.png.

Deterministic: copies the fixed image bundled in this repository, so both
runs write identical bytes.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
