def polacz_listy(lista1, lista2):
    nowa_lista = []

    for liczba in lista1:
        if liczba not in nowa_lista:
            nowa_lista.append(liczba)
    for liczba in lista2:
        if liczba not in nowa_lista:
            nowa_lista.append(liczba)

    print(nowa_lista)
    index = 0
    for wartosc in nowa_lista:
        nowa_lista[index] = wartosc ** 3
        index += 1

    return nowa_lista


lista_a = [1, 1, 5, 7, 9]
lista_b = [2, 3, 5, 8, 5, 10]

print(polacz_listy(lista_a, lista_b))