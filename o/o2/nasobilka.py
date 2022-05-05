
# odCislo = int(input("Zadaj od: "))
# doCislo = int(input("Zadaj do: "))
odCislo = 9
doCislo = 12

fero = int(len(str((doCislo**2-odCislo**2))))-1
medzeraZac = " "* fero
for i in range(odCislo, doCislo+1):
    print(f"{i:}", end=medzeraZac)
    if i == doCislo+1:
        print(i)
print()

for i in range(odCislo, doCislo+1):
    print(f"{i:{len(str(doCislo))}}", end=" -")
    for j in range(odCislo, doCislo+1):
        konec = i*j
        if konec == i*doCislo:
            konec = "\n"
        else:
            konec = ""
        medzera = len(str(doCislo**2)) + 1
        print(f"{i*j:{medzera}}", end=konec)
