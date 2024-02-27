def sprawdz_czy_istnieje(lista, wartosc):
    rezultat = False
    for pozycja in lista:
        if pozycja == wartosc:
            rezultat = True
            break
    return rezultat


lista_liczb = [71, 36, 15, 267, 943, 861, 942, 37, 812, 64]
szukana = 999
szukana2 = 943
szukana3 = 37
szukana4 = 1

print(sprawdz_czy_istnieje(lista_liczb, szukana))
print(sprawdz_czy_istnieje(lista_liczb, szukana2))
print(sprawdz_czy_istnieje(lista_liczb, szukana3))
print(sprawdz_czy_istnieje(lista_liczb, szukana4))