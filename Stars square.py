a = int(input("высота"))
b = int(input("ширина"))

i = 0
while i < a:
    j = 0
    while j <= b:
        print("*", end = "")
        j = j + 1
    print()
    i = i + 1


