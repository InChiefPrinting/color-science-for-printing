'''
\Delta E = \sqrt{(L_1-L_2)^2+(a_1-a_2)^2+(b_1-b_2)^2}
'''


import numpy as np

def delta_e_76(lab1, lab2):
    # Calculate Euclidean distance between two CIELAB color vectors
    # This is the original Delta E (1976) formula
    # lab1 and lab2 are 3-element arrays [L, a, b] in CIELAB color space
    # Returns a single number representing the perceived color difference
    return np.linalg.norm(lab1 - lab2)