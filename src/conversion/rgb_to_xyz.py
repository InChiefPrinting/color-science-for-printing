"""
rgb_to_xyz.py

Conversion from sRGB to CIE XYZ.

Pipeline:
Gamma RGB → Linear RGB → XYZ
"""

import numpy as np

from src.gamma.gamma_curve import inverse_gamma_srgb
from src.color_spaces.rgb import RGB
from src.color_spaces.xyz import XYZ


# sRGB → XYZ matrix (D65 white point)
SRGB_TO_XYZ = np.array([
    [0.4124564, 0.3575761, 0.1804375],
    [0.2126729, 0.7151522, 0.0721750],
    [0.0193339, 0.1191920, 0.9503041],
])


def rgb_to_xyz(rgb: RGB) -> XYZ:
    """
    Convert RGB object to XYZ color.

    Parameters
    ----------
    rgb : RGB
        RGB color instance

    Returns
    -------
    XYZ
        Converted XYZ color
    """

    values = rgb.as_array()

    # Convert to linear RGB if needed
    if not rgb.linear:
        values = inverse_gamma_srgb(values)

    xyz_values = SRGB_TO_XYZ @ values

    return XYZ(*xyz_values)