from src.icc.icc_parser import load_icc
from src.icc.matrix_builder import build_rgb_to_xyz_matrix

p = load_icc("data/icc_profiles/sRGB.icc")

print(build_rgb_to_xyz_matrix(p))