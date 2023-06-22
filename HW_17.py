def group_by_surname(list_of_enrollees: list) -> int:
    groups = {"A-I": 0, "J-P": 0, "Q-T": 0, "U-Z": 0}

    for enrollee in list_of_enrollees:
        first_letter = enrollee.split()[1][0]

        if first_letter.lower() <= 'i':
            groups["A-I"] += 1
        elif first_letter.lower() <= 'p':
            groups["J-P"] += 1
        elif first_letter.lower() <= 't':
            groups["Q-T"] += 1
        else:
            groups["U-Z"] += 1

    return groups

enrollees = ["Will Smith", "Ann Novak", "Taras Shevchenko", "Igor Velychko"]

print(group_by_surname(enrollees))
