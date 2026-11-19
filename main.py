#!/usr/bin/env python3
"""Write the 19 Nov 2026 world-news summary image to /output/entry.png.

Deterministic: copies the fixed image bundled in this repository, so both
runs write identical bytes.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)

# Verify the copy: the output must be byte-identical to the bundled image,
# so both runs write the same bytes. Fail loudly instead of silently
# shipping a truncated or mismatched file.
if sha256(SRC) != sha256(DST):
    raise SystemExit("entry.png copy mismatch: output differs from source")
print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
