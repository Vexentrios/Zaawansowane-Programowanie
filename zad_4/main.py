def porownaj_liczby(a, b, c):
    if a + b >= c:
        rezultat = True
    else:
        rezultat = False
    return rezultat


relacja = porownaj_liczby(2, 5, 9)
print(relacja)
relacja = porownaj_liczby(13, 5, 7)
print(relacja)