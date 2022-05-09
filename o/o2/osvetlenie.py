import tkinter

def svetlo(vstup):
    canvas.create_rectangle(100,100,150,150, fill="black")
    canvas.create_rectangle(160,100,210,150, fill="black")
    canvas.create_rectangle(220,100,270,150, fill="black")
    if vstup < 25:
        canvas.create_oval(100, 100, 150, 150, fill="white")
        canvas.create_oval(160, 100, 210, 150, fill="white")
        canvas.create_oval(220, 100, 270, 150, fill="white")
    elif 25 <= vstup < 50:
        canvas.create_oval(100, 100, 150, 150, fill="white")
        canvas.create_oval(220, 100, 270, 150, fill="white")
    elif 50 <= vstup < 70:
        canvas.create_oval(160, 100, 210, 150, fill="white")

canvas = tkinter.Canvas()
canvas.pack()

vstup = int(input("intenzita osvetlenia v luxoch: "))
svetlo(vstup)

canvas.mainloop()
