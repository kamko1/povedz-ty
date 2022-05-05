import turtle
import random

def kresli_hodiny():
    farba = f'#{random.randint(150, 255):02x}{random.randint(150, 255):02x}{random.randint(150, 255):02x}'
    pero.up()
    pero.setheading(0)
    pero.setpos(0, 0)
    pero.down()
    pero.dot(600, farba)
    pero.dot(20)
    ciara = 0
    for i in range(60):
        if ciara == 5 or ciara == 10:
            pero.setpos(0, 0)
            pero.up()
            pero.forward(280)
            pero.down()
            pero.width(3)
            pero.forward(30)
            pero.up()
            pero.right(6)
            ciara += 1
        elif 0 < ciara < 15:
            pero.setpos(0, 0)
            pero.up()
            pero.forward(280)
            pero.down()
            pero.width(0)
            pero.forward(30)
            pero.up()
            pero.right(6)
            ciara += 1
        elif ciara == 15 or ciara == 0:
            pero.setpos(0, 0)
            pero.up()
            pero.forward(280)
            pero.down()
            pero.width(5)
            pero.forward(30)
            pero.up()
            pero.right(6)
            ciara = 0
            ciara += 1

def rucicky(hod, min):
    #hodinova
    pero.setpos(0, 0), pero.setheading(90-hodiny*30-0.5*minuty), pero.down(), pero.width(6), pero.forward(222)
    #minutova
    pero.setpos(0, 0), pero.setheading(90-minuty*6), pero.down(), pero.width(4), pero.forward(280)

def vypis_cas(h, m):
    cas = f"{hodiny:02}:{minuty:02}"
    print(cas)
    pero.up()
    pero.setheading(0)
    pero.setpos(-100, 315)
    pero.down()
    pero.write(cas, font=("Courier New", 50, "bold"))

pero = turtle.Turtle()
tabula = turtle.Screen()
# tabula.tracer(0)
pero.speed(0)

hodiny = random.randint(1, 12)
minuty = random.randint(0, 59)

print(hodiny)
print(minuty)

vypis_cas(hodiny, minuty)
kresli_hodiny()
rucicky(hodiny, minuty)

pero.hideturtle()
tabula.mainloop()


