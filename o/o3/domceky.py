import turtle
import random
def nuholnik(n, a, farba):
    angle = 360//n
    pero.down()
    pero.fillcolor(farba)
    pero.begin_fill()
    for i in range(n):
        pero.forward(a)
        pero.left(angle)
    pero.end_fill()
    pero.up()
def domcek(f1, f2, a):
    nuholnik(4,a,f1)
    pero.left(90)
    pero.forward(a)
    pero.right(90)
    nuholnik(3,a,f2)
    pero.right(90)
    pero.forward(a)
    pero.left(90)
def n_farba():
    return f'#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}'
def ulica(rady, stlpce, a):
    for i in range(2, stlpce*2+2, 2):
        for k in range(rady):
            pero.setheading(0)
            domcek(n_farba(), n_farba(), a)
            pero.up()
            pero.setheading(0)
            pero.forward(a)
        pero.right(180)
        pero.forward(2 * a * stlpce)
        pero.right(90)
        pero.forward(2 * a)
        pero.right(90)
    pero.setpos(0, -i*a)
def nahodne_mesto(pocet):
    for i in range(pocet):
        pero.setheading(0)
        pero.left(random.randint(-10, 10))
        pero.setpos(random.randint(-333, 333), random.randint(-333, 333))
        domcek(n_farba(), n_farba(), random.randint(30, 70))
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.speed(0)
pero.up()
# ulica(7, 3, 30)
nahodne_mesto(30)
pero.hideturtle()
tabula.mainloop()
