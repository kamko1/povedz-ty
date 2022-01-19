d = open("diktat.txt", "r", encoding="UTF-8")
vstup = d.read()
pismena = "iíIÍyýYÝ"
pd = "_"

#"Kobyla býva v modernom obydlí. Sestra je veľmi bystrá."

makke = vstup.count("i") + vstup.count("í") + vstup.count("I") + vstup.count("Í")
tvrde = vstup.count("y") + vstup.count("ý") + vstup.count("Y") + vstup.count("Ý")

word_list = vstup.split()
pocet_slov = len(word_list)
print("Počet slov:",pocet_slov, end=", ")

percenta = (makke+tvrde)/pocet_slov*100
print("obtiažnosť:", percenta, "%")


def spocitaj():
    p = "iíIÍyýYÝ"
    for pismeno in p:
        pocet = 0
        for p in vstup:
            if pismeno == p:
                pocet += 1
        print(f"{pismeno}: {pocet}", end=", ")
spocitaj()

print()

def zamena(text, pd):
    for i in pismena:
        text = text.replace(i, pd)
    file = open("u.txt", "w", encoding="UTF-8")
    file.write(text)

zamena(vstup, pd)

