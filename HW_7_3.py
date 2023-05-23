
def second_index(search_str, search_index):

    second_index = search_str.find(search_index, search_str.find(search_index)+1)

    if second_index == -1:
        return None
    else:
        return second_index

search_str = input("Enter search string: ")
search_index = input("Enter search index: ")

print(second_index(search_str, search_index))