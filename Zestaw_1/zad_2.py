def basic_multiply(numbers):
    results = []
    for x in numbers:
        results.append(x*2)
    return results


def scalar_multiply(numbers):
    results = [x*2 for x in numbers]
    return results


data = [7, 3.5, 13, 3.14, 128]

changed1 = basic_multiply(data)
print(f"{changed1}\n")
changed2 = scalar_multiply(data)
print(changed2)
