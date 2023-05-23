import random
def common_elements(n):
    list_3 = [i for i in range(3, 3 * n + 1, 3)]
    list_5 = [i for i in range(5, 5 * n + 1, 5)]

    set_3 = set(list_3)
    set_5 = set(list_5)

    common_set = set_3.intersection(set_5)
    return common_set

n = int(input("Enter a number: "))
print(common_elements(n))








