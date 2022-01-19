import random

def roztried():
    otvor = open("studenti.txt", "r", encoding="UTF-8")
    citaj = otvor.read()
    meno = citaj.splitlines()
    girls = ""
    boys = ""
    for i in meno:
        if "ová" in i:
            girls += i +", "
        elif "ská" in i:
            girls += i +", "
        elif "ná" in i:
            girls += i +", "
        elif "ňak" in i:
            girls += i +", "
        elif "cká" in i:
            girls += i +", "
        else:
            boys += i +", "
    pocet_b = boys.split(", ")
    pocet_g = girls.split(", ")
    nahodny_b = random.choice(pocet_b)
    nahodny_g = random.choice(pocet_g)
    print(f" Dievčatá: ({girls})")
    print(f" Počet dievčat: {len(pocet_g)-1} ")
    print(f" Chlapci: ({boys})")
    print(f" Počet chlapcov: {len(pocet_b)-1} ")
    print(f" Zodpovedný za večerný program: {nahodny_b} a {nahodny_g}")
roztried()
