"""
delta_e_76.py

Basic Euclidean color difference in LAB space.
"""

import numpy as np
from src.color_spaces.lab import LAB


def delta_e_76(lab1: LAB, lab2: LAB) -> float:

    diff = lab1.as_array() - lab2.as_array()
    return np.linalg.norm(diff)