def co_druga(liczby):
    for x in range(1, len(liczby), 2):
        print(liczby[x])


dane_liczby1 = [x for x in range(10)]
dane_liczby2 = [11, 18, 26, 3, 91, 25, 36, 68, 256, 847]

co_druga(dane_liczby1)
print()
co_druga(dane_liczby2)