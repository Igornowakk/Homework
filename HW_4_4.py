h = int(input('Enter triangle height: '))
j = 1
for i in range(1, h + 1):
    line = (h - i) * ' '
    for k in range(j):
        line += '*'
    j += 2
    print(line)