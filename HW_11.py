def find_unique_value(numbers):
    counts = {}

    for value in numbers:
        counts[value] = counts.get(value, 0) + 1

    for value, count in counts.items():
        if count == 1:
            return value

    return None

numbers = [1, 2, 1, 1, 2]
print(find_unique_value(numbers))