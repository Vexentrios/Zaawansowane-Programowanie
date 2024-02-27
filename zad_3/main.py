def parzysta(liczba):
    if liczba % 2 == 0:
        rezultat = True
    else:
        rezultat = False
    return rezultat


funkcja = parzysta(13)
if funkcja:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

funkcja = parzysta(8)
if funkcja:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")