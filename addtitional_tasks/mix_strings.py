# You have two strings "Dogs like cats" and "Cats like dogs".
# Change theme, to make an output, after mixing them,
# or combining them in some other way (try to omit the easiest replace method :D), like:
# 1. "Dogs like dogs"
# 2. "Cats like cats"
# 3. "Dogs doesn't like cats, and cats doesn't like dogs"
# 4. f"Word dogs exist in this two sentences: {count_of_dogs_in_sentences} times.
# Word cats exist in this two sentences: {count_of_cats_in_sentences}" (not just put here numbers.
# Count it, as if you didn't know which sentences in variables)
# 5. "DCoagtss lliikkee cdaotgss" (mixing of chars from both sentences)

import random

dogs_string = "Dogs like cats"
cats_string = "Cats like dogs"

dogs_words = dogs_string.split()
cats_words = cats_string.split()

# 4th task:
no_of_dogs = dogs_string.lower().count('dogs') + cats_string.lower().count('dogs')
no_of_cats = cats_string.lower().count('cats') + dogs_string.lower().count('cats')

print(f"Word dogs exist in this two sentences: {no_of_dogs} times. "
      f"Word cats exist in this two sentences: {no_of_cats} times")

# 5th task
new_concatenation = ''

for i in range(len(dogs_string)):
    new_concatenation += dogs_string[i] + cats_string[i]
print(new_concatenation)

# 2nd task
dogs_words[0] = cats_words[0]
print(' '.join(dogs_words))

# 1st task
dogs_words = dogs_string.split()
cats_words[0] = dogs_words[0]
print(' '.join(cats_words))

# 3rd task
print(dogs_string[0:4] + " doesn't" + dogs_string[4:] + ' and ' + cats_string[0:4].lower() + " doesn't" + cats_string[4:])

