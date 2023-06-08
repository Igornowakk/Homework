def lchain(*iterables) -> list:
    lst_result = []

    for element in iterables:
        lst_result.extend(element)
    return lst_result

a = [1, 2, 3]
b = {'5': 5}
c = tuple()
d = (6, 7)
e = range(8, 10)
print(lchain(a, b, c, d, e))
