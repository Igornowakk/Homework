def generate_cube_numbers(n):
    for num in range(2, n + 1):
        num **= 3
        if num < n:
            yield num


gen = generate_cube_numbers(100)
print(next(gen))
print(next(gen))
print(next(gen))
