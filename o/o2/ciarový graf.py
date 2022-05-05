import tkinter
from math import *

canvas = tkinter.Canvas(width = 400, height = 400)
canvas.pack()

canvas.create_line(200, 30, 200, 400)
canvas.create_line(0, 200, 400, 200)

a = float(input("Zadajte koeficient a: "))
b = float(input("Zadajte koeficient b: "))
c = float(input("Zadajte koeficient c: "))
def kvad():
    d = (b**2) - (4*a*c)
    riesenie = 0
    if d > 0:
        print("2 riešenia, Diskriminant: ", d)
        riesenie += 2
    elif d == 0:
        print("1 riešenie, Diskriminant: ", d)
        riesenie += 1
    elif d < 0:
        print("Žiadne riešenie, Diskriminant:", d)
        canvas.destroy()
    if d > 0 or d == 0:
        x1 = (-b-sqrt(sqrt(b)-4*a*c)) / (2*a)
        x2 = (-b+sqrt(sqrt(b)-4*a*c)) / (2*a)
        print("x1 : ", round(x1))
        print("x2 : ", round(x2))
        canvas.create_text(200, 10, text=f"Počet riešení: {riesenie},      x1: {round(x1)},      x2: {round(x2)}")
        canvas.create_oval(200-3+x1, 200-3, 200+3+x1, 200+3, fill="red", outline="")
        canvas.create_oval(200-3+x2, 200-3, 200+3+x2, 200+3, fill="red", outline="")
        suradnice = []
        for x in range(-200, 200):
            y = -(a*x*x + b*x + c)
            suradnice.append(x + 200)
            suradnice.append(y + 200)
        canvas.create_line(suradnice, fill="green", width=2)
        canvas.mainloop()
kvad()
canvas.mainloop()

