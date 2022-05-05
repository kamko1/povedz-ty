file = open("vzdialenost.txt", "w", encoding="UTF-8")
trzba = 0
vzdialenost = 0
p = 1

while p !=0:
    file = open("vzdialenost.txt", "r", encoding="UTF-8")
    vstup = float(input("Napíšte vzdialenosť: "))
    file = open("vzdialenost.txt", "a", encoding="UTF-8")
    v = vstup
    if 0 < vstup <= 10:
        trzba += vstup*0.5
        vzdialenost += vstup
        file.write(str(v) + " km / " + str(v*0.5) + "€" + "\n")
        print(f"Cena za {round(vstup, 2)}km je {round(vstup*0.5, 2)}€")
    elif 10 < vstup <= 20:
        trzba += vstup*0.45
        vzdialenost += vstup
        file.write(str(v) + " km / " + str(v*0.45) + "€" + "\n")
        print(f"Cena za {round(vstup, 2)}km je {round(vstup*0.45, 2)}€")
    elif 20 < vstup <= 30:
        trzba += vstup*0.40
        vzdialenost += vstup
        file.write(str(v) + " km / " + str(v*0.40) + "€" + "\n")
        print(f"Cena za {round(vstup, 2)}km je {round(vstup*0.40, 2)}€")
    elif vstup > 30:
        trzba += vstup*0.35
        vzdialenost += vstup
        file.write(str(v) + " km / " + str(v*0.35) + "€" + "\n")
        print(f"Cena za {round(vstup, 2)}km je {round(vstup*0.35, 2)}€")
    elif vstup == 0:
        p = 0
        print(f"Dnes si najazdil {round(vzdialenost, 2)}km a zarobil si {round(trzba, 2)}€ / {round(trzba*1.16, 2)}$")
