
def pow(x):
    return x ** 2

def some_gen(begin, n, func):
    i = 0
    while i < n:
        yield begin
        begin = func(begin)
        i += 1


gen = some_gen(2, 4, pow)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

