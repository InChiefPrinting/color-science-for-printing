from src.icc.icc_parser import load_icc

profile = load_icc("data/icc_profiles/sRGB.icc")

print(profile)
print(profile.tags.keys())