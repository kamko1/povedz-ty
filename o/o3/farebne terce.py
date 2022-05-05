import turtle
import random
tabula = turtle.Screen()
pero = turtle.Turtle()
def kruhy():
    file = open("udaje.txt", "w")
    for k in range(1, 11):
        pero.down()
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        r = 50
        pero.up()
        pero.setpos(x, y)
        for i in range(1, 11):
            farba = f'#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}'
            pero.dot(r, farba)
            r -= 5
            file.write(str(f"{x} {y} {farba}"))
            file.write(str("\n"))
def nacitaj():
    p = 0
    file = open("udaje.txt", "r")
    citaj_riadky = file.readlines()
    for k in range(1, 11):
        strp = citaj_riadky[p].strip()
        a = strp.split()
        udaj_x = float(a[0])
        udaj_y = float(a[1])
        pero.down()
        x = udaj_x
        y = udaj_y
        r = 50
        pero.up()
        pero.setpos(x, y)
        for i in range(1, 11):
            strp = citaj_riadky[p].strip()
            a = strp.split()
            pero.down()
            udaj_farba = a[2]
            pero.dot(r, udaj_farba)
            r -= 5
            p += 1
kruhy()
pero.speed(0)
pero.hideturtle()
tabula.mainloop()
