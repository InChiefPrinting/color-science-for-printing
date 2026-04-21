"""
xyz_to_lab.py

Convert CIE XYZ to CIE LAB.

Reference white: D65
"""

import numpy as np

from src.color_spaces.xyz import XYZ
from src.color_spaces.lab import LAB


# D65 reference white
WHITE_POINT = np.array([0.95047, 1.00000, 1.08883])


def f(t):
    """
    Nonlinear function used in LAB transform.
    """

    delta = 6 / 29

    if t > delta**3:
        return t ** (1 / 3)
    else:
        return t / (3 * delta**2) + 4 / 29


def xyz_to_lab(xyz: XYZ) -> LAB:
    """
    Convert XYZ to LAB.
    """

    xyz_n = xyz.as_array() / WHITE_POINT

    fx = f(xyz_n[0])
    fy = f(xyz_n[1])
    fz = f(xyz_n[2])

    L = 116 * fy - 16
    a = 500 * (fx - fy)
    b = 200 * (fy - fz)

    return LAB(L, a, b)