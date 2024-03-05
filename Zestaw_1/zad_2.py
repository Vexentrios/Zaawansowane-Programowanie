def mnoznik_bazowy(liczby):
    wyniki = []
    for x in liczby:
        wyniki.append(x*2)
    return wyniki


def mnoznik_skladany(liczby):
    wyniki = [x*2 for x in liczby]
    return wyniki


dane = [7, 3.5, 13, 3.14, 128]

przetworzone = mnoznik_bazowy(dane)
print(f"{przetworzone}\n")
przetworzone = mnoznik_skladany(dane)
print(przetworzone)
