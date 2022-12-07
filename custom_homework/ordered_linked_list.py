class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class OrderedLinkedList:

    def __init__(self):
        self.head = None
        self.num_of_list_items = 0

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            current = self.current
            self.current = self.current.next
            return current
        raise StopIteration

    def print(self):
        for node in self:
            print(node, end='->')
        print()

    def add_node(self, value):
        node = Node(value)
        self.num_of_list_items += 1
        if self.head is None:
            self.head = node
        elif self.head.value > node.value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                if current.next.value > node.value:
                    node.next = current.next
                    current.next = node
                    break
                elif current.next.value < node.value:
                    current = current.next
                else:
                    break
            if current.next is None:
                current.next = node

    @staticmethod
    def find_middle(start, stop=None):
        if start:
            slow = start
            fast = start.next

            while fast != stop:
                fast = fast.next
                if fast != stop:
                    fast = fast.next
                    slow = slow.next

            return slow   # returns the middle object
        else:
            return None     # the list is empty, and we don't have any middle

    def binary_search(self, head, value):  # firstly, start item will be self.head <- we give this as argument

        start = head
        stop = None     # None comes after tail

        while True:
            middle = self.find_middle(start, stop)

            if middle is None:
                return False

            if middle.value == value:   # case in which our value is right iin the middle of the list
                return True

            elif value < middle.value:
                stop = middle

            elif value > middle.value:
                start = middle.next

            if not (stop is None or stop != start):
                break

        return False     # happens if value is not found during search


if __name__ == '__main__':
    the_list = OrderedLinkedList()
    the_list.add_node(10)
    the_list.print()
    the_list.add_node(5)
    the_list.print()
    the_list.add_node(7)
    the_list.print()
    the_list.add_node(13)
    the_list.print()
    the_list.add_node(7)
    the_list.print()
    the_list.add_node(15)
    the_list.print()

    # print(the_list.find_middle(the_list.head))
    print(the_list.binary_search(the_list.head, 7))