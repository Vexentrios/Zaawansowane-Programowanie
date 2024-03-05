def fuse_lists(list_a, list_b):
    new_list = []

    for number in list_a:
        if number not in new_list:
            new_list.append(number)
    for number in list_b:
        if number not in new_list:
            new_list.append(number)

    index = 0
    for value in new_list:
        new_list[index] = value ** 3
        index += 1

    return new_list


list1 = [1, 1, 5, 7, 9]
list2 = [2, 3, 5, 8, 5, 10]

print(fuse_lists(list1, list2))
