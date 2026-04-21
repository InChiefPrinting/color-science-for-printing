from src.icc.icc_parser import load_icc

profile = load_icc("data/icc_profiles/sRGB.icc")

print("White:", profile.tags["wtpt"])
print("Red:", profile.tags["rXYZ"])
print("Green:", profile.tags["gXYZ"])
print("Blue:", profile.tags["bXYZ"])