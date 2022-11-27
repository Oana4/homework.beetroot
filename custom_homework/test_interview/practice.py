# make a class with 2 variables, lists. When you iterate through the class,
# it should return each element of both lists.
# and the lists should be accessed only through properties

class ListContainer:

    def __init__(self, list_1=None, list_2=None):
        if list_1 is None:
            list_1 = ['a', 'b', 'c', 'd']
        if list_2 is None:
            list_2 = [1, 2, 3, 4, 5]
        self.list_1 = list_1
        self.list_2 = list_2
        self.iter_size = len(self.list_1) + len(self.list_2)
        self.iter_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_index < self.iter_size:
            if self.iter_index < len(self.list_1):
                current_item = self.list_1[self.iter_index]
            else:
                current_item = self.list_2[self.iter_index - len(self.list_1)]
            self.iter_index += 1
            return current_item
        raise StopIteration


container_1 = ListContainer()
for item in container_1:
    print(item)





