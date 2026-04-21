"""
tag_types.py

ICC tag type parsers.
"""

import struct


def s15fixed16(value_bytes):
    """
    Convert ICC s15Fixed16Number to float.
    """
    integer = struct.unpack(">i", value_bytes)[0]
    return integer / 65536.0


def parse_xyz_type(data):
    """
    Parse XYZType tag.
    """

    X = s15fixed16(data[8:12])
    Y = s15fixed16(data[12:16])
    Z = s15fixed16(data[16:20])

    return (X, Y, Z)