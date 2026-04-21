'''
f(t)=
\begin{cases}
t^{1/3} & t>\delta^3 \\
\frac{t}{3\delta^2}+\frac{4}{29}
\end{cases}
'''


import numpy as np

# Define the reference white point for CIE XYZ to CIELAB conversion
# These values correspond to D65 illuminant (standard daylight) with Y normalized to 100
WHITE = np.array([95.047, 100.0, 108.883])

def f(t):
    # Threshold constant: 6/29 ≈ 0.2069 (derived from (6/29)^3 ≈ 0.008856)
    delta = 6/29
    # For values above the threshold, use cubic root
    if t > delta**3:
        return t ** (1/3)
    # For small values (near zero), use linear function to avoid steep slope
    else:
        return t/(3*delta**2) + 4/29


def xyz_to_lab(xyz):
    # Step 1: Normalize XYZ values by the reference white point
    xyz = xyz / WHITE

    # Step 2: Apply the non-linear transformation function f() to each component
    fx, fy, fz = [f(v) for v in xyz]

    # Step 3: Compute CIELAB L* (lightness) channel
    # L ranges from 0 (black) to 100 (white)
    L = 116*fy - 16
    
    # Step 4: Compute CIELAB a* channel (green-red opponent colors)
    # Negative = green, Positive = red
    a = 500*(fx - fy)
    
    # Step 5: Compute CIELAB b* channel (blue-yellow opponent colors)
    # Negative = blue, Positive = yellow
    b = 200*(fy - fz)

    # Return LAB values as a numpy array
    return np.array([L, a, b])