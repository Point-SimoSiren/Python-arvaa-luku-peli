from random import randint
oikea_vastaus = randint(1,50)
print("Arvaa oikea luku - saat 7 yritystä")
arvauskerta = 0
while (arvauskerta < 7):
    syöte = input ("Arvaa luku välillä 1-50 - arvaus({0}): ".format(str(arvauskerta)))
    arvauskerta = arvauskerta+1
    arvaus = int(syöte)
    if arvaus < oikea_vastaus:
        print("Oikea luku on suurempi!")
    elif arvaus > oikea_vastaus:
        print("Oikea luku on pienempi")
    else:
        print("Onneksi olkoon - arvasit oikein!")
        break

syöte = input ("Peli päättyy")