class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def search_elem(self, element):
        if element not in self.items:
            raise ValueError(f"{element} is not in the list!")
        return element


my_stack = Stack()
my_stack.push("a")
my_stack.push("b")
my_stack.push("c")
print(my_stack.size())
print(my_stack.search_elem("c"))
print(my_stack.size())
print(my_stack.peek())