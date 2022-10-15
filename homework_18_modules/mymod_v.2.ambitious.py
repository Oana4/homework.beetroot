# this is the 3rd task
import os


def test(name):
    if not os.path.exists(name):
        raise OSError("The path doesn't exist!")
    with open(name) as file:
        counter = len(file.readlines())
        file.seek(0)
        c_counter = len(file.read())
    return f"For the number of lines we get {counter} lines, " \
           f"and meanwhile we get {c_counter} characters in {name} file."


print(test("mymod_v.2.ambitious.py"))

