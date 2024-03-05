def parzyste(liczby):
    for x in liczby:
        if x % 2 == 0:
            print(x)


dane_liczby1 = [x for x in range(10)]
dane_liczby2 = [11, 18, 26, 3, 91, 25, 36, 68, 256, 847]

parzyste(dane_liczby1)
print()
parzyste(dane_liczby2)
