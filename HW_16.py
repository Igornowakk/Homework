import string

def first_word(text: string) -> string:

    for element in text:
        if element in string.punctuation:
            text = text.replace(element, "")
    text = text.strip()

    space_index = text.find(' ')
    if space_index == -1:
        return text
    else:
        return text[:space_index]

text = "; Hello, World"
print(first_word(text))
