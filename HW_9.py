def add_one(list_number):
    number = int(''.join(map(str, list_number)))

    number += 1

    new_number = list(map(int, str(number)))

    return new_number

list_number = [9, 9, 9]
print(add_one(list_number))
