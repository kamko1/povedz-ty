import tkinter

w = 600
h = 600

canvas = tkinter.Canvas(width = w, height = h)
canvas.pack()
# vaha = float(input("Zadajte vašu hmotnosť: "))
# vyska = float(input("Zadajte vašu výšku (v cm): "))

vaha = 67
vyska = 187


def vypocitaj_bmi():
    m = vyska/100
    bmi = round(vaha/(m**2))
    if 0 <= bmi < 17.5:
        print("podvýživa")
        canvas.create_line()
    if 17.5 <= bmi <= 25:
        print("ideálna a zdravá váha")
    if 25 < bmi < 30:
        print("mierna nadváha")
    if 30 <= bmi <= 40:
        print("obezita")
    if bmi > 40:
        print("ťažká obezita")
    canvas.create_rectangle(0, 300, w/2.2, 400, fill = "yellow", outline="")
    canvas.create_rectangle(w/2.2, 300, w/1.6, 400, fill = "green", outline="")
    canvas.create_rectangle(w/1.6, 300, w/1.3, 400, fill = "orange", outline="")
    canvas.create_rectangle(w/1.3, 300, w, 400, fill = "red", outline="")
vypocitaj_bmi()
canvas.mainloop()



