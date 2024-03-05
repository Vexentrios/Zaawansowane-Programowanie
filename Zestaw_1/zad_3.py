def equal_numbers(numbers):
    for x in numbers:
        if x % 2 == 0:
            print(x)


numbers_list1 = [x for x in range(10)]
numbers_list2 = [11, 18, 26, 3, 91, 25, 36, 68, 256, 847]

equal_numbers(numbers_list1)
print()
equal_numbers(numbers_list2)
