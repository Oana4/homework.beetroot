my_tuple = 1, 2, 3, 1, 4
my_tuple_something = tuple(reversed(my_tuple))

print(my_tuple_something)

index = my_tuple_something.index(1)

print(len(my_tuple) - 1 - index)

my_string_tuple = "".join(list(map(str, my_tuple)))

print(my_string_tuple.rindex("1"))

