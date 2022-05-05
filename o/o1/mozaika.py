import tkinter
import random

canvas = tkinter.Canvas(width = 600, height = 400)
canvas.pack()

def kresli_mozaiku():
    file = open("parametre.txt", "w")
    nahodna_velkost = random.randrange(1,101)
    file.write(str(nahodna_velkost)+"\n")
    x = 0
    y = 0
    vyska = 400
    sirka = 600
    while y < vyska + nahodna_velkost:
        while x < sirka + nahodna_velkost:
            color = f"#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}"
            file.write(f"{color}\n")
            canvas.create_rectangle(x, y, x+nahodna_velkost, y+nahodna_velkost, fill = color, outline = "")
            x += nahodna_velkost
        x = 0
        y += nahodna_velkost

def vykresli():
    file = open("parametre.txt", "r")
    q = file.readlines()
    x = 0
    y = 0
    vyska = 400
    sirka = 600
    u = int(q[0])
    i = 1
    while y < vyska + u:
        while x < sirka + u:
            color = q[i].strip()
            print(color)
            canvas.create_rectangle(x, y, x+u, y+u, fill=color, outline=color)
            i += 1
            x += u
        x = 0
        y += u
# kresli_mozaiku()
vykresli()
canvas.mainloop()
