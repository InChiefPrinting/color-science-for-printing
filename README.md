# color-science-for-printing
color-science-for-printing. 

This repository reconstructs modern printing color management
from mathematical foundations.

No black box.
Only mathematics.




printing-color-science/
│
├── README.md
├── requirements.txt
├── setup.py
│
├── data/
│   ├── icc_profiles/
│   ├── color_samples/
│   └── test_images/
│
├── src/
│   ├── color_spaces/
│   │   ├── rgb.py
│   │   ├── xyz.py
│   │   ├── lab.py
│   │   └── cmyk.py
│   │
│   ├── conversion/
│   │   ├── rgb_to_xyz.py
│   │   ├── xyz_to_lab.py
│   │   ├── lab_to_xyz.py
│   │   └── gamut_mapping.py
│   │
│   ├── icc/
│   │   ├── icc_parser.py
│   │   └── profile_model.py
│   │
│   ├── color_difference/
│   │   ├── delta_e_76.py
│   │   ├── delta_e_94.py
│   │   └── delta_e_2000.py
│   │
│   ├── gamma/
│   │   └── gamma_curve.py
│   │
│   └── visualization/
│       ├── gamut_plot.py
│       └── lab_visualizer.py
│
├── notebooks/
│   ├── 01_rgb_to_xyz.ipynb
│   ├── 02_lab_space.ipynb
│   └── 03_delta_e_analysis.ipynb
│
└── examples/
    ├── convert_image.py
    └── compare_profiles.py


**Maintained by JeremyThierryChan**