import random

fav_word = input("Write a nice string: ")
all_chars = list(fav_word)

for i in range(5):
    random.shuffle(all_chars)
    print(''.join(all_chars))