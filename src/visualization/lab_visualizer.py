"""
Visualize LAB color distribution.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_ab_plane(lab_points):
    """
    Plot LAB a*b* plane.
    """

    lab_points = np.array(lab_points)

    a = lab_points[:, 1]
    b = lab_points[:, 2]

    plt.figure(figsize=(6,6))
    plt.scatter(a, b, s=5)

    plt.xlabel("a* (Green ←→ Red)")
    plt.ylabel("b* (Blue ←→ Yellow)")
    plt.title("LAB a*b* Plane")

    plt.axis("equal")
    plt.grid(True)
    plt.show()