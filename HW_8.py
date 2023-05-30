def roman_to_integer(roman_number):
    roman_meaning = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0

    for i in range(len(roman_number)):
        current_number = roman_meaning[roman_number[i]]

        if i < (len(roman_number) - 1) and roman_meaning[roman_number[i + 1]] > current_number:
            number -= current_number
        else:
            number += current_number

    return number

roman_number = ("MLXXIV")
print(roman_to_integer(roman_number))