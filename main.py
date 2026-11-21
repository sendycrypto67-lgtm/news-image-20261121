#!/usr/bin/env python3
"""Copy the news-image-20261121 entry to the output directory.

The entry is a single PNG file, entry.png, sitting next to this script.
This program checks that the file really is a PNG of the right size,
copies it to $MAKEFUN_OUTPUT_DIR (or /output when that is unset),
then reads the copy back and proves it is byte-for-byte the same file.
Only the Python standard library is used. No network, no randomness.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_SIDE = 1024
MAX_BYTES = 1048576


def fail(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def read_header(path):
    """Return (width, height) after checking the PNG signature and IHDR."""
    try:
        data = path.read_bytes()
    except FileNotFoundError:
        fail("source file not found: %s" % path)
    except OSError as exc:
        fail("cannot read %s: %s" % (path, exc))
    if len(data) < 33:
        fail("invalid PNG in %s: file too short" % path)
    if data[:8] != PNG_MAGIC:
        fail("invalid PNG in %s: bad PNG magic bytes" % path)
    length = struct.unpack(">I", data[8:12])[0]
    chunk = data[12:16]
    if chunk != b"IHDR":
        fail("invalid PNG in %s: first chunk is not IHDR" % path)
    if length != 13:
        fail("invalid PNG in %s: IHDR length is %d, expected 13" % (path, length))
    width, height = struct.unpack(">II", data[16:24])
    if width == 0 or height == 0:
        fail("invalid PNG in %s: zero dimension" % path)
    if width > MAX_SIDE or height > MAX_SIDE:
        fail("invalid PNG in %s: %dx%d exceeds %dx%d"
             % (path, width, height, MAX_SIDE, MAX_SIDE))
    # A well-formed PNG ends with the IEND chunk: four zero length bytes,
    # the four type bytes IEND, then four CRC bytes.
    if len(data) < 12 or data[-12:-8] != b"\x00\x00\x00\x00" \
            or data[-8:-4] != b"IEND":
        fail("invalid PNG in %s: missing IEND chunk" % path)
    return width, height, data


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        fail("source file missing: %s" % source)
    width, height, data = read_header(source)
    if len(data) > MAX_BYTES:
        fail("invalid PNG in %s: %d bytes exceeds %d"
             % (source, len(data), MAX_BYTES))
    source_hash = hashlib.sha256(data).hexdigest()

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    if dest.resolve() == source.resolve():
        fail("output path is the same file as the source: %s" % dest)
    shutil.copyfile(source, dest)

    out_width, out_height, out_data = read_header(dest)
    if out_width != width or out_height != height:
        fail("output dimensions %dx%d do not match source %dx%d"
             % (out_width, out_height, width, height))
    if len(out_data) != len(data):
        fail("output size %d does not match source size %d"
             % (len(out_data), len(data)))
    if hashlib.sha256(out_data).hexdigest() != source_hash:
        fail("output sha256 does not match source for %s" % dest)
    print("copied %s (%dx%d, %d bytes, sha256 %s) to %s"
          % (source, width, height, len(data), source_hash, dest))


if __name__ == "__main__":
    main()
