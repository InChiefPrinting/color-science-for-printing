from src.color_spaces.rgb import RGB
from src.conversion.rgb_to_xyz import rgb_to_xyz
from src.conversion.xyz_to_lab import xyz_to_lab

rgb = RGB(1.0, 0.0, 0.0)

xyz = rgb_to_xyz(rgb)
lab = xyz_to_lab(xyz)

print("XYZ:", xyz)
print("LAB:", lab)