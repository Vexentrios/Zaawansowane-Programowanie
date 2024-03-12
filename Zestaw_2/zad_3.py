def equal_number(number):
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result


checked_number1 = equal_number(13)
if checked_number1:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

checked_number2 = equal_number(8)
if checked_number2:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
