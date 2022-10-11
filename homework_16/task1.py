# my enumerate() syntax
def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


# my test
test_list = "abc"
for item_list in with_index(test_list):
    print(item_list)