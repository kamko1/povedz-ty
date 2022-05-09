import tkinter

def kresli_graf(typgrafu, hodnoty=[], farba='lightgray'):
    suradnice = []
    nula = 250
    krok_x = 600 // 30
    krok_y = 250 // 40
    x = 40
    if typgrafu == 'pozadie':
        for i in range(nula, 400, krok_y*5):
            platno.create_line(x,i,600,i, fill=farba)
            platno.create_text(20, i, text=((-i+250)//krok_y))
        for i in range(nula, 0, -krok_y*5):
            platno.create_line(x,i,600,i, fill=farba)
            platno.create_text(20, i, text=((250 - i)//krok_y))
        platno.create_line(x, 0, x, 400)
        platno.create_line(0,nula,600,nula)
    else:
        for y in hodnoty:
            suradnice.append((x, nula - y * krok_y))
            x += krok_x
        if typgrafu == 'ciarovy':
            platno.create_line(suradnice, fill=farba)
        elif typgrafu == 'izolovane_body':
            for x,y in suradnice:
                r = 2
                platno.create_oval(x-r, y-r, x+r, y+r, fill=farba, outline='')

teploty = []
priemerne = []

platno = tkinter.Canvas(width='600', height='400')
platno.pack()

subor = open("teploty.txt", "r", encoding="UTF-8")
file = subor.read().splitlines()

for i in range(-1,(len(file)),4):
    priemerne.append(float(file[i]))

for i in range(len(file)):
    if float(file[i]) not in priemerne:
        teploty.append(int(file[i]))

p_denna = ""
n_denna = ""
vsetky_t = ""

for teplota in teploty:
    n_denna += str(teplota) + ", "
for teplota in priemerne[1:]:
    p_denna += str(teplota) + ", "
for teplota in file:
    vsetky_t += teplota + ", "

print(f"Všetky teploty: {vsetky_t}")
print(f"Denné priemerné: {p_denna}")
print(f"Denné namerané: {n_denna}")
print(f"najvyššia priemerná teplota: {max(priemerne)}")

kresli_graf('pozadie')
kresli_graf("ciarovy", teploty, "red")
kresli_graf("izolovane_body", teploty, "red")
kresli_graf("ciarovy", priemerne, "blue")
kresli_graf("izolovane_body", priemerne, "blue")

platno.mainloop()
