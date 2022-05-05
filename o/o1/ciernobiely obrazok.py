import tkinter

n = int(input("Zadaj priblíženie obrázka (od 1 po 4): "))

def obrazok(velkost):
    riadok = []
    lenfarba = []
    for i in range(1, len(udaje)):
        riadok += udaje[i]
    for i in range(0, len(riadok)-1, 2):
        col = riadok[i]+riadok[i+1]
        farba = "#" + 3*col
        lenfarba += [farba]
    poc = 0
    for i in range(0, 260*velkost, velkost):
        for j in range(0, 400*velkost, velkost):
            canvas.create_rectangle(j, i, j+velkost, i+velkost, fill=lenfarba[poc], width=0)
            poc += 1

citajtext = open("sen.txt", "r")
udaje = citajtext.read().splitlines()
citajtext.close()

sirka, vyska = (int((udaje[0].split())[0]))*n, (int((udaje[0].split())[1]))*n
canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()

obrazok(n)
canvas.mainloop()
