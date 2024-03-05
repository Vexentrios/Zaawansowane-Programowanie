def check_if_exists(list, value):
    result = False
    for position in list:
        if position == value:
            result = True
            break
    return result


numbers = [71, 36, 15, 267, 943, 861, 942, 37, 812, 64]
searched1 = 999
searched2 = 943
searched3 = 37
searched4 = 1

print(check_if_exists(numbers, searched1))
print(check_if_exists(numbers, searched2))
print(check_if_exists(numbers, searched3))
print(check_if_exists(numbers, searched4))
