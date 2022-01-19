import random

# def generuj_heslo(a, b, c, d):
#     male_p = "qwertzuiopasdfghjklyxcvbnm"
#     velke_p = male_p.upper()
#     cisla = "0123456789"
#     znaky = "+=,.-§"
#     heslo = ""
#     for i in range(a):
#         heslo += random.choice(male_p)
#     for i in range(b):
#         heslo += random.choice(velke_p)
#     for i in range(c):
#         heslo += random.choice(cisla)
#     for i in range(d):
#         heslo += random.choice(znaky)
#     shuffle_heslo = ""
#     while len(heslo) > 0:
#         i = random.randrange(len(heslo))
#         shuffle_heslo += heslo[i]
#         heslo = heslo[:i] + heslo[i+1:]
#     return(shuffle_heslo)
#
# mp = int(input("Prosím, zadajte počet malých písmen: "))
# vp = int(input("Prosím, zadajte počet veľkých písmen: "))
# c = int(input("Prosím, zadajte počet číslic: "))
# z = int(input("Prosím, zadajte počet znakov: "))
#
# print(generuj_heslo(mp, vp, c, z))

#FULLY RANDOM PWASSWORD GENERATOR
def generuj_heslo(a, b, c, d):
   male_p = "qwertzuiopasdfghjklyxcvbnm"
   velke_p = male_p.upper()
   cisla = "0123456789"
   znaky = "+=,.-§"
   heslo = ""
   for i in range(a):
    heslo += random.choice(male_p)
   for i in range(b):
       heslo += random.choice(velke_p)
   for i in range(c):
       heslo += random.choice(cisla)
   for i in range(d):
       heslo += random.choice(znaky)
   shuffle_heslo = ""
   while len(heslo) > 0:
       i = random.randrange(len(heslo))
       shuffle_heslo += heslo[i]
       heslo = heslo[:i] + heslo[i+1:]
   return(shuffle_heslo)

print(generuj_heslo(random.randrange(1,10), random.randrange(1,10), random.randrange(1,10), random.randrange(1,10)))
