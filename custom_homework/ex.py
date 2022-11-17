square_generator = (num ** 2 for num in range(10))
square_list = [number ** 2 for number in range(10)]

print(square_generator)
print(square_list)

for num in square_generator:
    print(num)

print("\n")

for number in square_list:
    print(number)


# alternative to enumerate function
def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


print("\n")
test_list = "abc"
for item_list in with_index(test_list):
    print(item_list)
