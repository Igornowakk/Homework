import string

letters = string.ascii_letters
start, end = input("Enter two letters separated by a hyphen: ").split('-')

start_index = letters.index(start)
end_index = letters.index(end)

for i in range(start_index, end_index+1):
    print(letters[i], end=' ')