import random

n = random.randrange(3, 10)
list = [random.randrange(1, 100) for i in range(n)]
new_list = [list[0], list[2], list[-2]]
print(list)
print(new_list)
