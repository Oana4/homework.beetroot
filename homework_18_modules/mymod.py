# this is the 3rd task
import os


def count_lines(name):
    if not os.path.exists(name):
        raise OSError("The path doesn't exist!")
    with open(name) as file:
        counter = file.readlines()
    return len(counter)


def count_chars(name):
    if not os.path.exists(name):
        raise OSError("The path doesn't exist!")
    with open(name) as file:
        c_counter = file.read()
    return len(c_counter)


def test(name):
    if not os.path.exists(name):
        raise OSError("The path doesn't exist!")
    return f"For the number of lines we call count_lines and we get {count_lines(name)} lines, " \
           f"and meanwhile by calling count_chars we get {count_chars(name)} characters in {name} file."


print(test("mymod.py"))

