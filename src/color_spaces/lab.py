"""
lab.py

CIE L*a*b* color space representation.

LAB is a perceptually uniform color space designed
to approximate human vision.
"""

import numpy as np


class LAB:
    """
    LAB color representation.

    Parameters
    ----------
    L : float
        Lightness [0,100]

    a : float
        Green–Red axis

    b : float
        Blue–Yellow axis
    """

    def __init__(self, L, a, b):

        self.values = np.array([L, a, b], dtype=float)
        self._validate()

    # ---------------------------------------------
    def _validate(self):
        L = self.values[0]

        if not (0 <= L <= 100):
            raise ValueError("L must be within [0,100]")

    # ---------------------------------------------
    @property
    def L(self):
        return self.values[0]

    @property
    def a(self):
        return self.values[1]

    @property
    def b(self):
        return self.values[2]

    # ---------------------------------------------
    def as_array(self):
        return self.values.copy()

    # ---------------------------------------------
    def __repr__(self):
        return f"<LAB L={self.L:.2f}, a={self.a:.2f}, b={self.b:.2f}>"