import random
slova = ["vietor", "slnko", "voda", "diviak", "sova", "Jozef"]

def hra():
    pokusy = 10
    vyber = random.choice(slova)
    zasif = list(vyber)
    slovo = vyber
    pocet_pismen = len(slovo)-2
    slovo = zasif[0] + pocet_pismen * "." + zasif[-1]
    print (slovo)
    while slovo != vyber:
        hadaj = input("Prosím, zadaj písmeno: ")
        for i in range(len(vyber)):
            if vyber[i] == hadaj:
                slovo = slovo[0:i] + hadaj + slovo[i+1:]
        if hadaj not in vyber:
            pokusy -= 1
            print(f"Písmeno {hadaj} sa tam NEnachádza")
            print(f"Počet zostávajúcich pokusov: {pokusy}")
        else:
            print(f"Písmeno {hadaj} sa tam NAchádza")
            print(f"Počet zostávajúcich pokusov: {pokusy}")
        if pokusy < 1:
            print("PREHRAL SI!")
            break
        if slovo == vyber:
            print("VYHRAL SI!")
            break
        print(slovo)
hra()
