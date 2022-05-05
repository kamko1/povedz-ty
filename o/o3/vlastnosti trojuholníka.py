def zostrojenie(a, b, c):
    return str(c+b > a and a+b > c and c+a > b)

def rovnostranny(a, b, c):
    return str(a == b == c)

def rovnoramenny(a, b, c):
    return str(a == b != c or a == c != b or b == c != a)

def roznostranny(a, b, c):
    return str(a != b != c)

def pravouhly(a, b, c):
    return str(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2)

def precitaj(a, b, c):
    pis = open("trojuholnik_export.csv", "w")
    pis.write("a, b, c, Zostrojenie, Rovnostrannost, Rovnoramennost, Roznostrannost, pravouhlost\n")
    file = open("trojuholnik.csv", "r")
    for t in file:
        # a = t.split(",")
        # b = t.split(",")
        # c = t.split(",")
        a, b, c = int(a), int(b), int(c)
        text = f"{a}, {b}, {c}, "
        text += zostrojenie(a, b, c) + ",        "
        text += rovnostranny(a, b, c) + ",          "
        text += rovnoramenny(a, b, c) + ",          "
        text += roznostranny(a, b, c) + ",           "
        text += pravouhly(a, b, c) + "\n"
        pis.write(text)
precitaj(5, 8, 9)
