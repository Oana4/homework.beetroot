# You have a first list like values = [“one”, “two”, “three”, “four”, “five”] 
# and a second list indexes [1, 3, 5]. 
# You need to remove elements from first list which have an indexes from a second.


list_values = ['one', 'two', 'three', 'four', 'five', 'six']
list_indexes = [1, 5, 3]

list_indexes.sort()

for index in reversed(list_indexes):
    list_values.pop(index)

print(list_values)
