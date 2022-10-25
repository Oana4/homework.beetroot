from stack import Stack

# we use these lists as a trick to keep track of matching parentheses, after their index
open_symbols = ["[", "{", "("]
close_symbols = ["]", "}", ")"]


# this function searches through the entire list/string that we gave as argument;
# is looks only for parentheses, not another digits/letters (from the 2 lists above);
# it appends the open parentheses to our stack, so that they can easily be popped.
# if it finds an element from the close_symbols list, it searches for the corresponding match (the specific open symbol)
# and if they don't match, we simply return "Unbalanced" statement. If we go through the entire process, and we don't
# obtain an empty stack, it means that some symbol didn't have a corresponding pair, and we also return "Unbalanced"
def is_balanced(any_list):
    stack = Stack()
    for char in any_list:
        if char in open_symbols:
            stack.push(char)
        elif char in close_symbols:
            index = close_symbols.index(char)
            if ((stack.size() > 0) and
                    (open_symbols[index] == stack.peek())):
                stack.pop()
            else:
                return "Unbalanced"
    if stack.size() == 0:
        return "Balanced"
    else:
        return "Unbalanced"


print(is_balanced("{[()]}"))
print(is_balanced("{[]]]])"))
