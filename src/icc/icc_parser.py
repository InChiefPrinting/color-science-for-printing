"""
icc_parser.py

Minimal ICC profile parser.

Reads:
- header
- tag table
"""

import struct
from src.icc.profile_model import ICCProfile


def read_ascii(data):
    return data.decode("ascii").strip()


def parse_header(f, profile):

    f.seek(0)

    header = f.read(128)

    profile.size = struct.unpack(">I", header[0:4])[0]

    profile.device_class = read_ascii(header[12:16])
    profile.color_space = read_ascii(header[16:20])
    profile.pcs = read_ascii(header[20:24])


def parse_tag_table(f, profile):

    f.seek(128)

    tag_count = struct.unpack(">I", f.read(4))[0]

    for _ in range(tag_count):

        signature = read_ascii(f.read(4))
        offset = struct.unpack(">I", f.read(4))[0]
        size = struct.unpack(">I", f.read(4))[0]

        current_pos = f.tell()

        f.seek(offset)
        data = f.read(size)

        profile.add_tag(signature, data)

        f.seek(current_pos)


def load_icc(path):

    profile = ICCProfile()

    with open(path, "rb") as f:
        parse_header(f, profile)
        parse_tag_table(f, profile)

    return profile