"""
delta_e_2000.py

CIEDE2000 color difference implementation.

Reference:
Sharma et al., 2005
"""

import numpy as np
from src.color_spaces.lab import LAB


def delta_e_2000(lab1: LAB, lab2: LAB):

    L1, a1, b1 = lab1.as_array()
    L2, a2, b2 = lab2.as_array()

    # Step 1: Chroma
    C1 = np.sqrt(a1**2 + b1**2)
    C2 = np.sqrt(a2**2 + b2**2)
    C_bar = (C1 + C2) / 2

    # Step 2: G factor
    G = 0.5 * (1 - np.sqrt((C_bar**7) /
                           (C_bar**7 + 25**7)))

    a1p = (1 + G) * a1
    a2p = (1 + G) * a2

    C1p = np.sqrt(a1p**2 + b1**2)
    C2p = np.sqrt(a2p**2 + b2**2)

    # Step 3: Hue angles
    def hp(a, b):
        if a == 0 and b == 0:
            return 0
        angle = np.degrees(np.arctan2(b, a))
        return angle + 360 if angle < 0 else angle

    h1p = hp(a1p, b1)
    h2p = hp(a2p, b2)

    # Step 4: Differences
    dLp = L2 - L1
    dCp = C2p - C1p

    dhp = h2p - h1p
    if dhp > 180:
        dhp -= 360
    elif dhp < -180:
        dhp += 360

    dHp = 2 * np.sqrt(C1p * C2p) * \
        np.sin(np.radians(dhp / 2))

    # Step 5: Means
    L_bar = (L1 + L2) / 2
    C_bar_p = (C1p + C2p) / 2

    if abs(h1p - h2p) > 180:
        h_bar_p = (h1p + h2p + 360) / 2
    else:
        h_bar_p = (h1p + h2p) / 2

    # Step 6: Weighting functions
    T = (1
         - 0.17 * np.cos(np.radians(h_bar_p - 30))
         + 0.24 * np.cos(np.radians(2 * h_bar_p))
         + 0.32 * np.cos(np.radians(3 * h_bar_p + 6))
         - 0.20 * np.cos(np.radians(4 * h_bar_p - 63)))

    SL = 1 + (0.015 * (L_bar - 50)**2) / \
        np.sqrt(20 + (L_bar - 50)**2)

    SC = 1 + 0.045 * C_bar_p
    SH = 1 + 0.015 * C_bar_p * T

    # Step 7: Rotation term
    delta_theta = 30 * np.exp(
        -((h_bar_p - 275) / 25)**2)

    RC = 2 * np.sqrt(
        (C_bar_p**7) /
        (C_bar_p**7 + 25**7)
    )

    RT = -RC * np.sin(np.radians(2 * delta_theta))

    # Step 8: Final equation
    dE = np.sqrt(
        (dLp / SL)**2 +
        (dCp / SC)**2 +
        (dHp / SH)**2 +
        RT * (dCp / SC) * (dHp / SH)
    )

    return dE