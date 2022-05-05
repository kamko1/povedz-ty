import random

a = int(input("Zadajte počet malých písmen: "))
b = int(input("Zadajte počet veľkých písmen: "))
c = int(input("Zadajte počet čáslic: "))
d = int(input("Zadajte počet špeciálnych znakov: "))

def generuj_heslo(a, b, c, d):
    heslo = ""
    shuffle_heslo = ""
    mp = "qwertzuiopasdfghjklyxcvbnm"
    vp = mp.upper()
    cisla = "0123456789"
    znaky = "+=,.-§"
    for k in range(a):
        heslo += random.choice(mp)
    for k in range(b):
        heslo += random.choice(vp)
    for k in range(c):
        heslo += random.choice(cisla)
    for k in range(d):
        heslo += random.choice(znaky)
    while len(heslo) > 0:
        k = random.randrange(len(heslo))
        shuffle_heslo += heslo[k]
        heslo = heslo[:k] + heslo[k+1:]
    return(shuffle_heslo)
print(generuj_heslo(a, b, c, d))
