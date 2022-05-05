file = open("bus_vytazenost.txt", "r", encoding="UTF-8")
k = file.readlines()

kapacita = int(k[0])
print(f"Kapacita autobusu: {kapacita}")

pocet_zastavok = len(k[1:])
print(f"Počet zastávok: {pocet_zastavok}")

def bus():
    zastavky = ""
    pretazenie = 0
    m_p = []
    for i in k[1:]:
        nazov_z = i.split(" ", 2)
        zastavky += nazov_z[2].strip() + ", "
        s = i.strip()
        pocet_nastupujucich = int(s[0:2])
        pocet_vystupujucich = int(s[2:5])
        pretazenie += pocet_nastupujucich - pocet_vystupujucich
        if pretazenie > kapacita:
            print(f"Autobus prekročil kapacitu na: {nazov_z[2]}")
            m_p.append(pretazenie)
    print(f"Názvy zastávok: {zastavky}")
    print(f"Najväčšie preťaženie o: {max(m_p)-50}")
bus()
