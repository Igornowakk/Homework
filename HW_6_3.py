list_tuple = []
list_tuple.append(("yellow", 1))
list_tuple.append(("blue", 2))
list_tuple.append(("yellow", 3))
list_tuple.append(("blue", 4))
list_tuple.append(("red", 1))

new_dict = {}
for item in list_tuple:
    if item[0] not in new_dict:
        new_dict[item[0]] = [item[1]]
    else:
        new_dict[item[0]].append(item[1])

print(new_dict)
