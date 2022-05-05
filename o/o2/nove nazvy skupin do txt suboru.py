import random
pocet = int(input("Prosím, zadajte počet samohlások v mene kapely: "))
pocet_nazvov = int(input("Prosím, zadajte počet: "))
file = open("skupiny.txt", "w", encoding="UTF-8")
file = open("skupiny.txt", "r", encoding="UTF-8")

def nazov(n):
    pn = pocet_nazvov
    spoluhlasky = "bcdfghjklmnprstvwxz"
    samohlasky = "aeiouy"
    nazov = ""
    for i in range(pn):
        a = random.choice(samohlasky)
        b = random.choice(spoluhlasky)*n
        nazov += a.upper()
        nazov += b
        nazov += a
        nazov += "\n"
        file = open("skupiny.txt", "w", encoding="UTF-8")
        file.write(nazov)
        for f in range(1):
            file = open("skupiny.txt", "r", encoding="UTF-8")
            p = file.read()
            zoznam = p.split()
            if nazov in zoznam:
                None
            else:
                file = open("skupiny.txt", "a", encoding="UTF-8")
                file.write(nazov)
            for f in range(1):
                file = open("Sás.txt", "r", encoding="UTF-8")
                p = file.read()
                zoznam = p.split()
    print(nazov)
    return nazov
(nazov(pocet))
