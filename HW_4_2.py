lst = [1, 2, 3, 4, 5, 6]
a = len(lst)
y = len(lst) % 2

if y == 0:
    b = int(a) // 2
    c = lst[0:int(b)]
    d = lst[int(b):int(a)]
    print([c, d])
elif y == 1:
    b = int(a) // 2
    c = lst[0:(int(b) + 1)]
    d = lst[(int(b) + 1):int(a)]
    print([c, d])
else:
    print([[], []])

