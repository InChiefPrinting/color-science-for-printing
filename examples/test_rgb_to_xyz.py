from src.color_spaces.rgb import RGB
from src.conversion.rgb_to_xyz import rgb_to_xyz

rgb = RGB(1.0, 0.0, 0.0)  # pure red
xyz = rgb_to_xyz(rgb)

print(xyz)