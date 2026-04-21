"""
gamma_curve.py

Gamma correction models used in color science.

This module implements:
- sRGB gamma encoding
- sRGB gamma decoding (linearization)
- Visualization of gamma response curves

Author: Printing Color Science Project
"""

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------
# sRGB Gamma Decoding (Inverse Gamma)
# ------------------------------------------------------
def inverse_gamma_srgb(rgb):
    """
    Convert nonlinear sRGB values to linear RGB.

    Parameters
    ----------
    rgb : array-like
        sRGB values in range [0, 1]

    Returns
    -------
    numpy.ndarray
        Linear RGB values
    """

    rgb = np.asarray(rgb, dtype=float)

    # Piecewise function defined by sRGB standard
    mask = rgb <= 0.04045

    linear = np.empty_like(rgb)

    # Linear segment
    linear[mask] = rgb[mask] / 12.92

    # Power-law segment
    linear[~mask] = ((rgb[~mask] + 0.055) / 1.055) ** 2.4

    return linear


# ------------------------------------------------------
# sRGB Gamma Encoding
# ------------------------------------------------------
def gamma_encode_srgb(linear_rgb):
    """
    Convert linear RGB values to nonlinear sRGB.

    Parameters
    ----------
    linear_rgb : array-like
        Linear RGB values

    Returns
    -------
    numpy.ndarray
        Gamma encoded sRGB values
    """

    linear_rgb = np.asarray(linear_rgb, dtype=float)

    mask = linear_rgb <= 0.0031308

    srgb = np.empty_like(linear_rgb)

    # Linear part
    srgb[mask] = 12.92 * linear_rgb[mask]

    # Power-law part
    srgb[~mask] = 1.055 * (linear_rgb[~mask] ** (1 / 2.4)) - 0.055

    return srgb


# ------------------------------------------------------
# Visualization
# ------------------------------------------------------
def plot_gamma_curve():
    """
    Plot sRGB gamma encoding and decoding curves.
    """

    x = np.linspace(0, 1, 500)

    encoded = gamma_encode_srgb(x)
    decoded = inverse_gamma_srgb(encoded)

    plt.figure(figsize=(6, 5))

    plt.plot(x, encoded, label="Gamma Encode (Linear → sRGB)")
    plt.plot(encoded, decoded, "--", label="Gamma Decode (sRGB → Linear)")

    plt.title("sRGB Gamma Curve")
    plt.xlabel("Input")
    plt.ylabel("Output")

    plt.legend()
    plt.grid(True)

    plt.show()


# ------------------------------------------------------
# Standalone Test
# ------------------------------------------------------
if __name__ == "__main__":
    plot_gamma_curve()