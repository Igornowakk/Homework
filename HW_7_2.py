def correct_sentence(a):
     if not a.endswith('.'):
        a += '.'
     return a.capitalize()

a = input("Enter a sentence: ")
print(correct_sentence(a))
