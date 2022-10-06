#  You have a list of strings [“article”, “cat”, “bat”].
#  Use map function, to make all words in a new list - start from the capital.

random_list = ["article", "cat", "bat"]


def capitalize_all_words(some_list):
    return list(map(lambda item: item.capitalize(), some_list))


print(capitalize_all_words(random_list))
