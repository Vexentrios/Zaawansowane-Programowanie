def jump_by_two(numbers):
    for x in range(1, len(numbers), 2):
        print(numbers[x])


numbers_data1 = [x for x in range(10)]
numbers_data2 = [11, 18, 26, 3, 91, 25, 36, 68, 256, 847]

jump_by_two(numbers_data1)
print()
jump_by_two(numbers_data2)
