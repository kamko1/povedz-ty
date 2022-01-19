

file = open("bus_vytazenost.txt", "r", encoding="UTF-8")
q = file.readlines()

kapacita = int(q[0])
print(f"Kapacita autobusu: {kapacita}")


pocet_zastavok = len(q[1:])
print(f"Pocet zastávok: {pocet_zastavok}")



zastavky = []
for o in q[1:]:
    nazov = o.split()
    rozdel = nazov[2:4]
    d = str(rozdel)
    zastavky.append(d)
print("Názvy zastávok:", *zastavky, sep=" ")

obsadenost = 0
for j in q[1:]:
    pocet_nastupujucich = j.strip()
    n = pocet_nastupujucich[0:2]
    no = int(n)
    pocet_vystupujucich = j.strip()
    v = pocet_vystupujucich[2:5]
    vo = int(v)
    obsadenost += no
    obsadenost -= vo
    if obsadenost > kapacita:
        print("Autobus prekročil kapacitu na zástávke ",(d))

