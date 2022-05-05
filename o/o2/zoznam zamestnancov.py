otvor = open("mena_zamestnancov.txt", "r", encoding="UTF-8")
vystup = open("vystup.txt", "w", encoding="UTF-8")
riadky = otvor.readlines()
pocet_r = len(riadky)
list = list(riadky)
pocet_m = pocet_r//2

for v in range(len(list)):
    list[v] = list[v].replace("\n", "")

dm = 0
dp = 0
a = 0
for k in range(pocet_m):
    cele_m = list[a]  + " " + list[a+pocet_m]
    dlzka_m = len(list[a])-1
    dlzka_p = len(list[a+pocet_m])-1
    a += 1
    vystup = open("vystup.txt", "r", encoding="UTF-8")
    vystup = open("vystup.txt", "a", encoding="UTF-8")
    vystup.write(cele_m + "\n")
    if dlzka_m > dm:
        dm = 0
        dm += dlzka_m
    else:
        None
    if dlzka_p > dp:
        dp = 0
        dp += dlzka_p
    else:
        None

print(f"Počet mien: {pocet_m}")
print(f"Dĺžka najdlhšieho mena: {dm}")
print(f"Dĺžka najdlhšieho priezviska: {dp}")
