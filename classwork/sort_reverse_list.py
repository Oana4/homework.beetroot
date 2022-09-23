list_values = ['one', 'two', 'three', 'four', 'five', 'six']
list_indexes = [1, 5, 3]

list_indexes.sort()

for index in reversed(list_indexes):
    list_values.pop(index)

print(list_values)
