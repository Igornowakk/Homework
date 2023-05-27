my_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 35
pairs = []

for i in range(len(my_list)):
    for j in range(i +1, len(my_list)):
        if my_list[i] + my_list[j] == target:
            pairs.append((my_list[j], my_list[i]))
            pairs.append((my_list[i], my_list[j]))

print(pairs)

