def MolesToGrams():
    print("Moles to Grams")


def GramsToMoles():
    print("Moles to Grams")


def MolesToParticles():
    print("Moles to Grams")


def ParticlesToMoles():
    print("Moles to Grams")


Empty = "Empty"
H = ("1", "1.008")
He = ("2", "4.003")
Li = ("3", "6.941")
Be = ("4", "9.012")
B = ("5", "10.811")
C = ("6", "12.011")
N = ("7", "14.007")
O = ("8", "16")
F = ("9", "18.998")
Ne = ("10", "20.180")
Na = ("11", "22.99")
Mg = ("12", "24.305")
Al = ("13", "26.982")
Si = ("14", "28.086")
P = ("15", "30.974")
S = ("16", "32.066")
Cl = ("17", "35.453")
Ar = ("18", "39.948")
K = ("19", "39.098")
Ca = ("20", "40.078")
Sc = ("21", "44.956")
Ti = ("22", "47.867")
V = ("23", "50.996")
Cr = ("24", "51.996")
Mn = ("25", "54.938")
Fe = ("26", "55.845")
Co = ("27", "58.933")
Ni = ("28", "58.693")
Cu = ("29", "63.546")
Zn = ("30", "65.38")
Ga = ("31", "69.723")
Ge = ("32", "72.631")
As = ("33", "74.922")
Se = ("34", "78.971")
Br = ("35", "79.904")
Kr = ("36", "83.789")
Rb = ("37", "85.468")
Sr = ("38", "87.62")
Y = ("39", "88.906")
Zr = ("40", "91.224")
Nb = ("41", "92.908")
Mo = ("42", "95.95")
Tc = ("43", "98.907")
Ru = ("44", "101.07")
Rh = ("45", "102.906")
Pd = ("46", "106.42")
Ag = ("47", "107.868")
Cd = ("48", "112.414")
In = ("49", "114.818")
Sn = ("50", "118.711")
Sb = ("51", "121.760")
Te = ("52", "127.6")
I = ("53", "126.904")
Xe = ("54", "131.294")
Cs = ("55", "132.905")
Ba = ("56", "137.828")
La = ("57", "138.905")
Ce = ("58", "140.116")
Pr = ("59", "140.980")
Nd = ("60", "144.243")
Pm = ("61", "144.913")
Sm = ("62", "150.36")
Eu = ("63", "151.964")
Gd = ("64", "157.25")
Tb = ("65", "158.925")
Dy = ("66", "162.5")
Ho = ("67", "164.930")
Er = ("68", "167.359")
Tm = ("69", "168.934")
Yb = ("70", "173.055")
Lu = ("71", "174.967")
Hf = ("72", "178.49")
Ta = ("73", "180.84")
W = ("74", "183.84")
Re = ("75", "186.207")
Os = ("76", "190.23")
Ir = ("77", "192.217")
Pt = ("78", "195.085")
Au = ("79", "118.711")
Hg = ("80", "200.592")
Tl = ("81", "204.383")
Pb = ("82", "107.2")
Bi = ("83", "208.980")
Po = ("84", "208.982")
At = ("85", "209.987")

Rn = ("86", "118.711")
Fr = ("87", "118.711")
Ra = ("88", "118.711")
Ac = ("89", "118.711")
Th = ("90", "118.711")
Pa = ("91", "118.711")
U = ("92", "118.711")
Np = ("93", "118.711")
Pu = ("94", "118.711")
Am = ("95", "118.711")
C = ("96", "118.711")
Bk = ("97", "118.711")
Cf = ("98", "118.711")
Es = ("99", "118.711")
Fm = ("100", "118.711")
Md = ("100", "118.711")
No = ("100", "118.711")
Lr = ("100", "118.711")
Rf = ("100", "118.711")
Db = ("100", "118.711")
Sg = ("100", "118.711")
Bh = ("100", "118.711")
Hs = ("100", "118.711")
Mt = ("100", "118.711")
Ds = ("100", "118.711")
Rg = ("100", "118.711")
Cn = ("100", "118.711")
Nh = ("100", "118.711")
Fl = ("100", "118.711")
Mc = ("100", "118.711")
Lv = ("100", "118.711")
Ts = ("100", "118.711")
Og = ("100", "118.711")

Elements = [
    Empty,
    H,
    He,
    Li,
    Be,
    B,
    C,
    N,
    O,
    F,
    Ne,
    Na,
    Mg,
    Al,
    Si,
    P,
    S,
    Cl,
    Ar,
    K,
    Ca,
    Sc,
    Ti,
    V,
    Cr,
    Mn,
    Fe,
    Co,
    Ni,
    Cu,
    Zn,
    Ga,
    Ge,
    As,
    Se,
    Br,
    Kr,
    Rb,
    Sr,
    Y,
    Zr,
    Nb,
    Mo,
    Tc,
    Ru,
    Rh,
    Pd,
    Ag,
    Cd,
    In,
    S,
    Sb,
    Te,
    I,
    Xe,
    Cs,
    Ba,
    La,
    Ce,
    Pr,
    Nd,
    Pm,
    Sm,
    Eu,
    Gd,
    Tb,
    Dy,
    Ho,
    Er,
    Tm,
    Yb,
    Lu,
    Hf,
    Ta,
    W,
    Re,
    Os,
    Ir,
    Pt,
    Au,
    Hg,
    Tl,
    Pb,
    Bi,
    Po,
    At,
    Rn,
    Fr,
    Ra,
    Ac,
    Th,
    Pa,
    U,
    Np,
    Pu,
    Am,
    C,
    Bk,
    Cf,
    Es,
    Fm,
    Md,
    No,
    Lr,
    Rf,
    Db,
    Sg,
    Bh,
    Hs,
    Mt,
    Ds,
    Rg,
    Cn,
    Nh,
    Fl,
    Mc,
    Lv,
    Ts,
    Og
]

print("What conversion type would you like? /n 1: Moles to Grams /n 2: Grams to Moles /n 3: Moles to Particles /n 4: Particles to Moles")
ConversionType = input()
print("What element are you converting? Only enter element symbol")
ElemType = input()



if ConversionType == 1:
    print("pain")
elif ConversionType == 2:
    print("pain")
elif ConversionType == 3:
    print("pain")
elif ConversionType == 4:
    print("pain")
