import tkinter

def riadok():
    for riadok in file:
        obrazok.append(riadok.split())
    print(obrazok)
    x = 0
    y = 0
    while y < vyska:
        while x < sirka:
            if int(obrazok[y][x]) > 0:
                canvas.create_rectangle(x, y, x, y, fill="black", outline="black")
            else:
                canvas.create_rectangle(x, y, x, y, fill="white", outline="white")
            x += 1
        x = 0
        y += 1

def preklop():
    for riadok in file:
        obrazok.append(riadok.split()[::-1])
    canvas.delete('all')
    x = 0
    y = 0
    while y < vyska:
        while x < sirka:
            if int(obrazok[y][x]) > 0:
                canvas.create_rectangle(x, y, x, y, fill="black", outline="black")
            else:
                canvas.create_rectangle(x, y, x, y, fill="white", outline="white")
            x += 1
        x = 0
        y += 1

obrazok = []
file = open("preklopenie_obrazka.txt", "r")
citaj_rozmery = file.readline().split()
sirka = int(citaj_rozmery[0])
vyska = int(citaj_rozmery[1])

canvas = tkinter.Canvas(width = sirka, height = vyska)
canvas.pack()

# button1 = tkinter.Button(text='Preklopiť', command = preklop)
# button1.pack()

canvas.bind('<Button-1>', preklop)

riadok()

canvas.mainloop()



