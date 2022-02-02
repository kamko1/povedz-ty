import tkinter

canvas = tkinter.Canvas(width = 300, height = 300)
canvas.pack()

def kresli_stvorceky():
    file = open("stvorceky_udaje.csv", "r")
    file.readline()
    for p in file:
        x, y, farba, strana = p.split(";")
        x, y, strana = int(x), int(y), int(strana)
        canvas.create_rectangle(x, y, x+strana, y+strana, fill = farba, outline = "")


kresli_stvorceky()
canvas.mainloop()
