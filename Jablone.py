import turtle
import random

platno = turtle.Screen()
pero = turtle.Turtle()
pero.speed(0)

x = 0
y = 0

def strom(vyska, jablka):
    global x
    global y
    pero.setheading(0)
    pero.color("brown")
    pero.setpos(x, y)
    pero.down()
    pero.begin_fill()
    pero.left(90)
    pero.width(vyska/6)
    pero.forward(vyska*1.2)
    pero.dot(vyska, "green")
    for i in range (jablka):
        pero.up()
        pero.setheading(random.randint(0, 360))
        vzdialenost = random.randint(0, vyska//2)
        pero.forward(vzdialenost)
        pero.dot(vyska/10, "red")
        pero.left(180)
        pero.forward(vzdialenost)

def sad():
    global x
    global y
    ps = 0
    for  k in range(riadky):
        for i in range(pocet_s):
            strom(random.randint(30, 100), random.randint(0, 20))
            pero.setpos(x, y)
            x += 88
            ps += 1
            if ps == pocet_s:
                y -= 100
                x = 0
                ps = 0

pocet_s = int(platno.textinput("Sad", "Zadaj pocet stromov v riadku"))
riadky = int(platno.textinput("Sad", "Zadaj pocet riadkov"))

try:
    pocet_s = float(pocet_s)
    riadky = float(riadky)
except ValueError:
    raise ValueError("Zadali ste nečíselnú hodnotu.")
if pocet_s < 0 or riadky < 0:
    raise ValueError('Zadali ste zápornú hodnotu.')


sad()


pero.hideturtle()
platno.mainloop()
