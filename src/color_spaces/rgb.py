"""
rgb.py

Definition of RGB color space object.

This module represents RGB colors as mathematical entities
instead of raw tuples.

Key concepts:
- RGB values may be gamma encoded or linear
- Explicit state tracking avoids color science mistakes
"""

import numpy as np


class RGB:
    """
    RGB color representation.

    Parameters
    ----------
    r, g, b : float
        Channel values in range [0, 1]

    linear : bool
        True if values are linear-light RGB
        False if values are gamma-encoded (sRGB)
    """

    def __init__(self, r, g, b, linear=False):

        self.values = np.array([r, g, b], dtype=float)
        self.linear = linear

        self._validate()

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------
    def _validate(self):
        """Ensure RGB values are valid."""

        if np.any(self.values < 0) or np.any(self.values > 1):
            raise ValueError("RGB values must be in range [0,1]")

    # --------------------------------------------------
    # Accessors
    # --------------------------------------------------
    @property
    def r(self):
        return self.values[0]

    @property
    def g(self):
        return self.values[1]

    @property
    def b(self):
        return self.values[2]

    # --------------------------------------------------
    # Conversion helpers
    # --------------------------------------------------
    def as_array(self):
        """Return RGB as numpy array."""
        return self.values.copy()

    # --------------------------------------------------
    # String representation
    # --------------------------------------------------
    def __repr__(self):
        mode = "Linear RGB" if self.linear else "Gamma RGB"
        return f"<RGB {self.values} ({mode})>"