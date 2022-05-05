import random
import tkinter
canvas = tkinter.Canvas(width = 800, height = 600)
canvas.pack()


a = int(input("Prosím, zadaj počet: "))
c5 = []
c4 = []
for i in range(a):
    cislo = random.randint(100, 1000)
    if cislo % 5==0:
        c5.append(cislo)
    elif cislo % 4==0:
        c4.append(cislo)
print(c4)
print(c5)
def graf():
    y = len(c5)
    y1 = len(c4)
    canvas.create_line(50, 50, 50, 400)
    canvas.create_line(20, 370, 400, 370)
    canvas.create_text(95, 390, text= "deliteľné 5")
    canvas.create_rectangle(70, 370, 120, 370-y, fill = "purple")
    canvas.create_text(165, 390, text= "deliteľné 4")
    canvas.create_rectangle(140, 370, 190, 370-y1, fill = "black")
    canvas.create_text(95, 370-y-10, text = y)
    canvas.create_text(165, 370-y1-10, text = y1)
graf()

canvas.mainloop()
