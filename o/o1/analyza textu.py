zoznam_pismen = "aáäbcčdďeéfghiíjklĺľmnňoóôpqrŕsštťuúvwxyýzž"
text = "Aj v tomto školskom roku naše gymnázium ponúka možnosť vzdelávať sa vo voľnočasovom programe s názvom Akadémia veľkých diel"

for pismeno in zoznam_pismen:
    pocet = 0
    for znak in text:
        if pismeno == znak.lower():
            pocet += 1
        if pismeno == znak.upper():
            pocet += 1
    print(f"{pismeno}: {pocet}")
