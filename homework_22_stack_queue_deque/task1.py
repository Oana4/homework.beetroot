from stack import Stack


def reverse_list(any_list):
    stack_for_reverse = Stack()
    for item in any_list:
        stack_for_reverse.push(item)
    reversed_list = ''
    while not stack_for_reverse.isEmpty():
        reversed_list += stack_for_reverse.pop()
    return reversed_list


print(reverse_list("Such a beautiful day"))
print(reverse_list("12345"))