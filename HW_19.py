def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num != i and num % i == 0:
            return False
    return True
def prime_generator(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num

gen = prime_generator(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


