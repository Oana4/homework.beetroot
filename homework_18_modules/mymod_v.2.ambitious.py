# this is the 3rd task
import os


def test(name):
    if not os.path.exists(name):
        raise OSError("The path doesn't exist!")
    with open(name) as file:
        line_counter = len(file.readlines())
        file.seek(0)
        char_counter = len(file.read())
    return f"For the number of lines we get {line_counter} lines, " \
           f"and meanwhile we get {char_counter} characters in {name} file."


print(test("mymod_v.2.ambitious.py"))

