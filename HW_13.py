def popular_words(text, *words):
    lst = ['.', ",", '!', '?', ';', ':']
    for element in lst:
        text = text.replace(element, "")

    text = text.lower()
    text_list = text.split()

    dict_popular_words = {}
    for word in text_list:
        if word in words:
            if word in dict_popular_words:
                dict_popular_words[word] += 1
            else:
                dict_popular_words[word] = 1

    return dict_popular_words


text = "Hello, world, hello. World is beautiful."
print(popular_words(text, "hello", "world", "is"))