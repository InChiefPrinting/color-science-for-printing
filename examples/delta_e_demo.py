from src.color_spaces.lab import LAB
from src.color_difference.delta_e_2000 import delta_e_2000

lab1 = LAB(50, 2.6772, -79.7751)
lab2 = LAB(50, 0.0, -82.7485)

print(delta_e_2000(lab1, lab2))