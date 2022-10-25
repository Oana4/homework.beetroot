class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def str(self):
        return self.items

    def search_elem(self, element):
        if element not in self.items:
            raise ValueError(f"{element} is not in the list!")
        return element


my_queue = Queue()
my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")
print(my_queue.str())
print(my_queue.search_elem("b"))
print(my_queue.search_elem("a"))
print(my_queue.str())