def MolesToGrams():
    print("Moles to Grams")
    print("What element are you converting? Only enter element symbol")
    ElemType = input()
    MpG = Elements[ElemType]
    print("How many moles would you like to convert?")
    MolAmnt = int(input())
    print(MolAmnt * MpG)


def GramsToMoles():
    print("Moles to Grams")
    print("What element are you converting? Only enter element symbol")
    ElemType = input()
    MpG = Elements[ElemType]
    print("How many grams would you like to convert?")
    GrmAmnt = int(input())
    print(GrmAmnt * (1/MpG))


def MolesToParticles():
    print("Moles to Grams")
    Mole = 6.02 * 10**23
    print("How many moles would you like to convert?")
    MolAmnt = float(input())
    print(MolAmnt * Mole)


Elements = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.941,
    "Be": 9.012,
    "B": 10.811,
    "C": 12.011,
    "N": 14.007,
    "O": 16,
    "F": 18.998,
    "Ne": 20.180,
    "Na": 22.99,
    "M": 24.305,
    "Al": 26.982,
    "Si": 28.086,
    "P": 30.974,
    "S": 32.066,
    "Cl": 35.453,
    "Ar": 39.948,
    "K": 39.098,
    "Ca": 40.078,
    "Sc": 44.956,
    "Ti": 47.867,
    "V": 50.996,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.933,
    "Ni": 58.693,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.723,
    "Ge": 72.631,
    "As": 74.922,
    "Se": 78.971,
    "Br": 79.904,
    "Kr": 83.789,
    "Rb": 85.468,
    "Sr": 87.62,
    "Y": 88.906,
    "Zr": 91.224,
    "Nb": 92.908,
    "Mo": 95.95,
    "Tc": 98.907,
    "Ru": 101.07,
    "Rh": 102.906,
    "Pd": 106.42,
    "Ag": 107.868,
    "Cd": 112.414,
    "In": 114.818,
    "Sn": 118.711,
    "Sb": 121.760,
    "Te": 127.6,
    "I": 126.904,
    "Xe": 131.294,
    "Cs": 132.905,
    "Ba": 137.828,
    "La": 138.905,
    "Ce": 140.116,
    "Pr": 140.980,
    "Nd": 144.243,
    "Pm": 144.913,
    "Sm": 150.36,
    "Eu": 151.964,
    "Gd": 157.25,
    "Tb": 158.925,
    "Dy": 162.5,
    "Ho": 164.930,
    "Er": 167.359,
    "Tm": 168.934,
    "Yb": 173.055,
    "Lu": 174.967,
    "Hf": 178.49,
    "Ta": 180.84,
    "W": 183.84,
    "Re": 186.207,
    "Os": 190.23,
    "Ir": 192.217,
    "Pt": 195.085,
    "Au": 118.711,
    "Hg": 200.592,
    "Tl": 204.383,
    "Pb": 107.2,
    "Bi": 208.980,
    "Po": 208.982,
    "At": 209.987,
    "Rn": 222.018,
    "Fr": 223.020,
    "Ra": 226.025,
    "Ac": 227.028,
    "Th": 232.038,
    "Pa": 231.036,
    "U ": 238.029,
    "Np": 237.048,
    "Pu": 244.06,
    "Am": 243.061,
    "Cm ": 247.070,
    "Bk": 247.070,
    "Cf": 251.080,
    "Es": 254,
    "Fm": 257.095,
    "Md": 258.1,
    "No": 259.101,
    "Lr": 262,
    "Rf": 261,
    "Db": 262,
    "Sg": 266,
    "Bh": 264,
    "Hs": 269,
    "Mt": 281,
    "Ds": 280,
    "Rg": 285,
    "Cn": 285,
    "Nh": 286,
    "Fl": 289,
    "Mc": 286,
    "Lv": 293,
    "Ts": 294,
    "Og": 294
}

print("What conversion type would you like? \n 1: Moles to Grams \n 2: Grams to Moles \n 3: Moles to Particles")
ConversionType = int(input())

if ConversionType == 1:
    MolesToGrams()
elif ConversionType == 2:
    GramsToMoles()
elif ConversionType == 3:
    MolesToParticles()
