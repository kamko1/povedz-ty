import tkinter
import random

canvas = tkinter.Canvas(width=700, height=500, bg='lightblue')
canvas.pack()

def kresli_kopec():
    farby = ["lawngreen", "darkgreen", "yellowgreen", "lightgreen", "springgreen", "mediumspringgreen", "olivedrab", "darkolivegreen", "olive", "darkseagreen"]
    print(farby)
    x = 0
    udaje = []
    udaje.append(x)
    lb = random.randint(250, 500)
    vrchol = random.randint(150, 450)
    y = lb
    udaje.append(lb)
    print(f"súradnice prvého bodu {udaje}")
    print(f"vrchol: {vrchol}")
    if lb > vrchol:
        print("stupa")
        while lb > vrchol:
            nahodna_y = random.randint(1, 11)
            y -= nahodna_y
            lb -= nahodna_y
            nahodna_x = random.randint(10, 50)
            x += nahodna_x
            udaje.append(x), udaje.append(y)
        while x <= 700:
            nahodna_y = random.randint(1, 11)
            lb += nahodna_y
            y += nahodna_y
            nahodna_x = random.randint(10, 50)
            x += nahodna_x
            udaje.append(x), udaje.append(y)
    elif vrchol > lb:
        print("klesa")
        while lb < vrchol:
            nahodna_y = random.randint(1, 11)
            y += nahodna_y
            lb += nahodna_y
            nahodna_x = random.randint(10, 50)
            x += nahodna_x
            udaje.append(x), udaje.append(y)
        while x <= 700:
            nahodna_y = random.randint(1, 11)
            lb -= nahodna_y
            y -= nahodna_y
            nahodna_x = random.randint(10, 50)
            x += nahodna_x
            udaje.append(x), udaje.append(y)
    udaje.append(700), udaje.append(500), udaje.append(0), udaje.append(500)
    print(udaje)
    canvas.create_polygon(udaje, fill=random.choice(farby))


def prekresli(event):
    canvas.delete('all')
    for i in range(10):
        kresli_kopec()

kresli_kopec()
canvas.bind_all('<space>', prekresli)
canvas.mainloop()
