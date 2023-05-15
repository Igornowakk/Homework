lst = [0]
new_lst = []
num_zeros = 0

for element in lst:
    if element != 0:
            new_lst.append(element)
    else:
            num_zeros += 1

new_lst.extend([0] * num_zeros)

print(new_lst)







