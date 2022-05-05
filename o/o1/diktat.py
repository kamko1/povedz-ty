text = "Kobyla býva v modernom obydlí. Sestra je veľmi bystrá."
p = "_"
makke = text.count("i") + text.count("í") + text.count("I") + text.count("Í")
tvrde = text.count("y") + text.count("ý") + text.count("Y") + text.count("Ý")

def pocet():
    iy = "iíIÍyýYÝ"
    for pismeno in iy:
        pocet = 0
        for iy in text:
            if pismeno == iy:
                pocet += 1
        print(f"{pismeno}: {pocet}", end=" | ")

def zamenenie(text, z):
    iy = "iíIÍyýYÝ"
    for k in iy:
        text = text.replace(k, z)
    print()
    print(text)

zamenenie(text, p)
pocet()
print()

text = text.split()
pocet_slov = len(text)
percenta = round((makke+tvrde)/pocet_slov*100, 2)
print("Počet slov: ", pocet_slov)
print("obtiažnosť: ", percenta, "%")
