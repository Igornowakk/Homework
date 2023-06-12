
def is_even():
    n = 0
    while True:
        if n & 1:
            yield("False")
        else:
            yield("True")
        n += 1

gen = is_even()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
