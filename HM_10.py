def is_palindrome(sentence):
    lst = ['.', ",", '!', '?', ';', ':', ' ']
    for element in lst:
        sentence = sentence.replace(element, "")
    sentence = sentence.lower()

    return sentence == sentence[::-1]

sentence = "A man, a plan, a canal: Panama"
print(is_palindrome(sentence))