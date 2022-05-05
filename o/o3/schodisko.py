import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()
def schody(v, p):
    s = 63 - 2 * vyska
    cv = v * p
    cs = s * p
    pero.fillcolor("green")
    pero.begin_fill()
    for i in range(p):
        pero.up()
        pero.left(90)
        pero.forward(v)
        pero.right(90)
        pero.forward(s)
    pero.right(90)
    pero.forward(cv)
    pero.right(90)
    pero.forward(cs)
    pero.penup()
    pero.left(90)
    pero.forward(20)
    pero.end_fill()
    pero.hideturtle()
    if 13 > vyska > 8:
        pero.write(f"Rampové schodisko: výška = {cv}cm, šírka = {cs}cm")
        print("Typ schodiska: rampové")
    if 15 > vyska >= 13:
        pero.write(f"Mierne schodisko: výška = {cv}cm, šírka = {cs}cm")
        print("Typ schodiska: mierne")
    if 18 > vyska >= 15:
        pero.write(f"Normálne schodisko: výška = {cv}cm, šírka = {cs}cm")
        print("Typ schodiska: normálne")
    if 20 > vyska >= 18:
        pero.write(f"Strmé schodisko: výška = {cv}cm, šírka = {cs}cm")
        print("Typ schodiska: strmé")
    if 25 >= vyska >= 20:
        pero.write(f"Rebríkové schodisko: výška = {cv}cm, šírka = {cs}cm")
        print("Typ schodiska: rebríkové")
vyska = int(tabula.textinput("Ta sak schody", "Zadajte výšku schodu:"))
pocet = int(tabula.textinput("Ta sak schody", "Zadajte počet schodov:"))
sirka = 63 - 2 * vyska
schody(vyska, pocet)
tabula.mainloop()
