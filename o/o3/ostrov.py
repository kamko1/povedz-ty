import tkinter
import random

canvas = tkinter.Canvas(width = 500, height = 500, background="blue")
canvas.pack()
canvas.create_oval(20, 250, 480, 800, fill="green", outline="")

def poloha(kde):
    x = kde.x
    y = kde.y
    if (x-250)**2 + (y-500)**2 <= 230**2:
        clovek(x, y)
    else:
        rybka(x, y)

def clovek(x, y):
    farba_c = random.choice(["yellow", "red", "white", "black"])
    canvas.create_oval(x-10, y-10, x+10, y+10, fill=farba_c, outline="")
    canvas.create_polygon(x, y+10, x+10, y+40, x-10, y+40, fill=farba_c, outline="")

def rybka(x, y):
    farba_r = random.choice(["yellow", "pink", "white", "purple"])
    canvas.create_oval(x-5, y-5, x+15, y+10, fill=farba_r, outline="")
    canvas.create_polygon(x+15, y+4, x+25, y-3, x+25, y+13, fill=farba_r, outline="")

canvas.bind('<Button-1>', poloha)

canvas.mainloop()
