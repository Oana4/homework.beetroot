chosen_string = input('Please, choose your favorite string and type it here: ')
words_chosen_str = chosen_string.split()

inventory = {}

for word in words_chosen_str:
    inventory[word] = words_chosen_str.count(word)

print(inventory)