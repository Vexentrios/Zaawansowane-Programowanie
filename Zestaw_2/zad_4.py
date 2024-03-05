def compare_numbers(a, b, c):
    if a + b >= c:
        result = True
    else:
        result = False
    return result


relation1 = compare_numbers(2, 5, 9)
print(relation1)
relation2 = compare_numbers(13, 5, 7)
print(relation2)
