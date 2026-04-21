"""
Build RGB → XYZ matrix from ICC primaries.
"""

import numpy as np


def build_rgb_to_xyz_matrix(profile):

    r = profile.tags["rXYZ"]
    g = profile.tags["gXYZ"]
    b = profile.tags["bXYZ"]

    M = np.array([
        [r[0], g[0], b[0]],
        [r[1], g[1], b[1]],
        [r[2], g[2], b[2]],
    ])

    return M