"""
xyz.py

CIE XYZ color space definition.

XYZ is device-independent and represents
human visual response.
"""

import numpy as np


class XYZ:
    """
    XYZ color representation.
    """

    def __init__(self, X, Y, Z):

        self.values = np.array([X, Y, Z], dtype=float)

        self._validate()

    def _validate(self):
        if np.any(self.values < 0):
            raise ValueError("XYZ values must be non-negative")

    @property
    def X(self):
        return self.values[0]

    @property
    def Y(self):
        return self.values[1]

    @property
    def Z(self):
        return self.values[2]

    def as_array(self):
        return self.values.copy()

    def __repr__(self):
        return f"<XYZ {self.values}>"