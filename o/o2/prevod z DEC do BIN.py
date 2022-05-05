try:
    vstup = int(input("Zadaj prirodzené číslo v desiatkovej sústave: "))
    pocet_b = int(input("Zadaj počet bajtov: "))
    prevod = bin(vstup)
    upraveny_prevod = prevod[2:]
    vysledok = ""
    pocet_c = len(prevod) - 2
    zvys = (pocet_b * 8) - pocet_c
    dopis = f"0" * zvys
    vysledok += dopis
    vysledok += upraveny_prevod
    upraveny_vysledok = " ".join(vysledok[i:i+8] for i in range(0, len(vysledok), 8))

except ValueError:
    print('Nezadali ste číselný údaj')
else:
    if vstup <= 0:
        print("Nezadali ste prirodzené číslo!")
    else:
        print(f"binárny zápis: {upraveny_vysledok}")
