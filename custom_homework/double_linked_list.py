class Node:

    def __init__(self, value, next_node=None, prev_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_list_items = 0

    def __iter__(self):
        self.item_iterated = self.head
        return self

    def __next__(self):
        if self.item_iterated is not None:
            current_item_iterated = self.item_iterated
            self.item_iterated = self.item_iterated.next
            return current_item_iterated
        raise StopIteration

    def add_tail_node(self, value):
        node = Node(value)
        self.num_of_list_items += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def add_head_node(self, value):
        node = Node(value)
        self.num_of_list_items += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def add_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        elif value < self.head.value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            previous = None
            while current is not None:
                if current.next is None:
                    current.next = node
                    break
                elif value < current.next.value:
                    node.next = current.next
                    current.next = node
                    break
                elif value > current.next.value:
                    previous = current
                    current = current.next
            else:
                previous.next = node
                node.next = None


my_linked_list = LinkedList()
# print(my_linked_list.head)  # None
# print(my_linked_list.tail)  # None
# print(my_linked_list.num_of_list_items)     # 0

# my_linked_list.add_tail_node("holiday")
# my_linked_list.add_tail_node("winter")
# my_linked_list.add_tail_node("favorite season")
#
# my_linked_list.add_head_node("Christmas")

my_linked_list.add_node(2)
my_linked_list.add_node(3)
my_linked_list.add_node(4)
my_linked_list.add_node(1)

for item in my_linked_list:
    print(item)

# output:
# Christmas
# holiday
# winter
# favorite season

# (works as expected)
