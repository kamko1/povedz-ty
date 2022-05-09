import tkinter
import turtle
from time import strftime

canvas = tkinter.Canvas(width = 1152, height = 864, bg="black")
canvas.pack()
pero = turtle.RawTurtle(canvas)
canvas.create_rectangle(-600, -600, 600, 600, fill="black")
pero.speed(0)

rychlost = 0
hodnota = 0

def rychlost_budik():
    ciara = -1
    pero.setpos(-250,-50)
    pero.setheading(258)
    pero.down()
    for i in range(41):
        if ciara < 4:
            pero.setpos(-250,-50)
            pero.up()
            pero.forward(160)
            pero.down()
            pero.width(3)
            pero.pencolor("white")
            pero.begin_fill()
            pero.forward(14)
            pero.up()
            pero.right(5)
            ciara += 1
        elif ciara == 4:
            pero.setpos(-250,-50)
            pero.up()
            pero.forward(156)
            pero.down()
            pero.width(5)
            pero.pencolor("coral")
            pero.forward(18)
            pero.up()
            pero.right(5)
            ciara += 1
            ciara = 0

def otacky_budik():
    ciara = -1
    pero.up()
    pero.setpos(0,0)
    pero.down()
    pero.setheading(210)
    pero.down()
    for i in range(41):
        if ciara < 4:
            pero.setpos(0,0)
            pero.up()
            pero.forward(160)
            pero.down()
            pero.width(3)
            pero.pencolor("white")
            pero.begin_fill()
            pero.forward(14)
            pero.up()
            pero.right(6)
            ciara += 1
        elif ciara == 4:
            pero.setpos(0,0)
            pero.up()
            pero.forward(156)
            pero.down()
            pero.width(5)
            pero.pencolor("coral")
            pero.forward(18)
            pero.up()
            pero.right(6)
            ciara += 1
            ciara = 0
        pero.up()
    pero.pencolor("coral")
    pero.setpos(0,0), pero.dot(15), pero.setheading(210), pero.down(), pero.width(6), pero.forward(150)
    pero.up()

def mod():
    global hodnota
    hodnota += 1
    if hodnota == 1:
        canvas.create_rectangle(-75, 120, -35, 150, fill="black")
        canvas.create_text(-55, 135, text="NORMAL", fill="white", font=("impact", 9, "normal"))
    elif hodnota == 2:
        canvas.create_rectangle(-75, 120, -35, 150, fill="black")
        canvas.create_text(-55, 135, text="SPORT", fill="white", font=("impact", 9, "normal"))
    elif hodnota == 3:
        canvas.create_rectangle(-75, 120, -35, 150, fill="black")
        canvas.create_text(-55, 135, text="SPORT\nPLUS", fill="white", font=("impact", 9, "normal"))
        hodnota -= 4
    elif hodnota == 0:
        canvas.create_rectangle(-75, 120, -35, 150, fill="black")
        canvas.create_text(-55, 135, text="---", fill="white", font=("impact", 9, "normal"))

def zmazat():
    global rychlost
    pero.right(180)
    pero.pencolor("#181818")
    pero.width(8)
    pero.down()
    pero.forward(150)
    #zmaz mod
    canvas.create_rectangle(-30, 121, 80, 150, fill="black")
    canvas.create_text(25, 135, text=f"{rychlost} km/h", fill="white", font=("impact", 20, "normal"))

def palubna_doska():
    global rychlost
    #lavybudik
    pero.setpos(-250,-50)
    pero.dot(350, "#181818")
    pero.dot(30, "black")
    pero.dot(15, "coral")
    pero.up()
    #pravy_budik
    pero.setpos(250, -50)
    pero.dot(350, "#181818")
    canvas.create_oval(150, 150, 330, 270, fill="black")
    canvas.create_rectangle(240, 150, 400, 270, fill="black")
    cas = strftime("%H:%M")
    canvas.create_text(275, 162, text=cas, fill="white", font=("impact", 15, "normal"))
    canvas.create_text(275, 185, text="5802 km", fill="white", font=("impact", 15, "normal"))
    canvas.create_text(285, 40, text="SEN - Palubná doska", fill="white", font=("impact", 15, "normal"))
    pero.up()
    #otackometer
    pero.setpos(0,0)
    pero.dot(350, "maroon")
    pero.dot(30, "black")
    pero.up()
    canvas.create_oval(-110, 120, -30, 200, fill="black")
    canvas.create_oval(110, 120, 30, 200, fill="black")
    canvas.create_rectangle(-70, 120, 70, 200, fill="black")
    canvas.create_text(0, -25, text=f"GT2RS", fill="white", font=("Comic Sans MS", 10, "italic", "bold"))
    #prevod_stupen
    canvas.create_rectangle(-10, 40, 10, 70, fill="black")
    canvas.create_text(0, 55, text="1", fill="white", font=("impact", 17, "normal", "bold"))
    #a_rychlost
    canvas.create_text(-55, 135, text="---", fill="white", font=("impact", 9, "normal"))
    canvas.create_text(25, 135, text=f"{rychlost} km/h", fill="white", font=("impact", 20, "normal"))

def rucicky():
    #rychlost
    pero.pencolor("coral")
    pero.setpos(-250, -50), pero.setheading(258-rychlost*0.5), pero.down(), pero.width(6), pero.forward(150)

def stupen():
    global rychlost
    if rychlost < 57:
        canvas.create_rectangle(-10, 40, 10, 70, fill="black")
        canvas.create_text(0, 55, text="1", fill="white", font=("impact", 17, "normal", "bold"))
    if rychlost > 57:
        canvas.create_rectangle(-10, 40, 10, 70, fill="black")
        canvas.create_text(0, 55, text="2", fill="white", font=("impact", 17, "normal", "bold"))
    if rychlost > 105:
        canvas.create_rectangle(-10, 40, 10, 70, fill="black")
        canvas.create_text(0, 55, text="3", fill="white", font=("impact", 17, "normal", "bold"))
    if rychlost > 149:
        canvas.create_rectangle(-10, 40, 10, 70, fill="black")
        canvas.create_text(0, 55, text="4", fill="white", font=("impact", 17, "normal", "bold"))
    if rychlost > 203:
        canvas.create_rectangle(-10, 40, 10, 70, fill="black")
        canvas.create_text(0, 55, text="5", fill="white", font=("impact", 17, "normal", "bold"))
    if rychlost > 264:
        canvas.create_rectangle(-10, 40, 10, 70, fill="black")
        canvas.create_text(0, 55, text="6", fill="white", font=("impact", 17, "normal", "bold"))
    if rychlost > 320:
        canvas.create_rectangle(-10, 40, 10, 70, fill="black")
        canvas.create_text(0, 55, text="7", fill="white", font=("impact", 17, "normal", "bold"))

def rychlost_minus():
    global rychlost
    if rychlost == 0:
        rychlost -= 0
        print("šak zaraď R-ko keď chceš cúvať ne")
    else:
        rychlost -= 5
    zmazat()
    stupen()
    pero.setheading(258)
    pero.pencolor("coral")
    pero.setpos(-250, -50),pero.dot(30, "black"), pero.dot(15, "coral"), pero.setheading(258-rychlost*0.5), pero.down(), pero.width(6), pero.forward(150)

def rychlost_plus():
    global rychlost
    if rychlost == 345:
        rychlost += 0
        print("čo si ty raketa či čo, šak auto ma 342 maximulku")
    else:
        rychlost += 5
    zmazat()
    stupen()
    pero.setheading(258)
    pero.pencolor("coral")
    pero.setpos(-250, -50),pero.dot(30, "black"), pero.dot(15, "coral"), pero.setheading(258-rychlost*0.5), pero.down(), pero.width(6), pero.forward(150)

button1 = tkinter.Button(text='zrýchliť', command=rychlost_plus)
button1.pack()

button2 = tkinter.Button(text='spomaliť', command=rychlost_minus)
button2.pack()

button3 = tkinter.Button(text='driving mod', command=mod)
button3.pack()

palubna_doska()
otacky_budik()
rychlost_budik()
rucicky()

canvas.mainloop()
