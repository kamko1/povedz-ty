import tkinter
import random

canvas = tkinter.Canvas(width = 600, height = 600)
canvas.pack()

def hod1(x, f1, f2):
    canvas.create_polygon(50+x, 200, 60+x, 190, 150+x, 190, 160+x, 200, 105+x, 310, fill=f1)
    canvas.create_polygon(50+x, 400, 60+x, 410, 150+x, 410, 160+x, 400, 105+x, 290, fill=f1)
    canvas.create_polygon(60+x, 205, 150+x, 205, 105+x, 290, fill=f2)
    canvas.create_polygon(60+x, 395, 150+x, 395, 105+x, 310, fill=f2)

def hod2(x1, f1, f2):
    canvas.create_polygon(150+x1, 200, 160+x1, 190, 250+x1, 190, 260+x1, 200, 205+x1, 310, fill=f2)
    canvas.create_polygon(150+x1, 400, 160+x1, 410, 250+x1, 410, 260+x1, 400, 205+x1, 290, fill=f2)
    canvas.create_polygon(160+x1, 205, 250+x1, 205, 205+x1, 290, fill=f1)
    canvas.create_polygon(160+x1, 395, 250+x1, 395, 205+x1, 310, fill=f1)

def hodiny():
    farba_zoznam = ["orange", "yellow", "green", "red", "blue"]
    farba1 = random.choice(farba_zoznam)
    farba_zoznam.remove(farba1)
    farba2 = random.choice(farba_zoznam)
    farba_zoznam.remove(farba2)
    print(farba1)
    print(farba2)
    print(farba_zoznam)
    for i in range(3):
        hod1(i*200, farba1, farba2)
    for k in range(2):
        hod2(k*200, farba1, farba2)

hodiny()
canvas.mainloop()
