import turtle
import math
a = int(input("strana a: ")) * 10
b = int(input("strana b: ")) * 10
c = int(input("strana c: ")) * 10
def trojuholnik(x, y, z):
    cos_x = (y ** 2 + z ** 2 - x ** 2) / (2 * y * z)
    alfa = round(math.degrees(math.acos(cos_x)))
    cos_y = (x ** 2 + z ** 2 - y ** 2) / (2 * x * z)
    beta = round(math.degrees(math.acos(cos_y)))
    cos_z = (y ** 2 + x ** 2 - z ** 2) / (2 * x * y)
    gama = round(math.degrees(math.acos(cos_z)))
    print(f"alfa: {alfa}")
    print(f"beta: {beta}")
    print(f"gama: {gama}")
    pero.forward(c)
    pero.write("B")
    pero.right(180+beta)
    pero.forward(a)
    pero.write("C")
    pero.right(180+gama)
    pero.forward(b)
    pero.up()
    pero.forward(13)
    pero.write("A")
    pero.setheading(270)
    pero.forward(15)
    pero.setheading(0)
    pero.write(f"a={a/10}, b={b/10}, c={c/10}")
    pero.setheading(270)
    pero.forward(10)
    pero.setheading(0)
    pero.write(f"alfa={alfa}, beta={beta}, gama={gama}")
try:
    vypocet = a + b + c
except ValueError:
    raise ValueError('Zadali ste nečíselnú hodnotu pre dĺžku strany obdĺžnika.')
if a <= 0 or b <= 0 or c <= 0:
    raise ValueError('Zadali ste záporné číslo alebo nulu.')
if c+b < a or a+b < c or c+a < b:
    print("takýto trojuholník nedokážem vytvoriť")
screen = turtle.Screen()
pero = turtle.Turtle()
pero.speed(0)
trojuholnik(a, b, c)
pero.hideturtle()
screen.mainloop()
