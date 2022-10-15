import os
from task1 import OpenFile

# simple test
with OpenFile("new_test.txt", "w") as file:
    file.write("this is also a test")
print(file.closed)      # returns True, correct

# should raise an error because I call read() method while it supports writing mode
with OpenFile("new_test.txt", "w") as file:
    print(file.read())
# does the expected thing: ERROR:root:An exception has occurred
# io.UnsupportedOperation: not readable

if os.path.exists("homework_01/test1.txt"):
    with OpenFile("homework_01/test1.txt", 'r') as test_file:
        print(test_file.readlines())
else:
    raise OSError("The path doesn't exist!")

# add an intentional typo in method to raise an error
with OpenFile("2nd_test.txt", "w") as file:
    file.writes("Hello world!")
# output: AttributeError: '_io.TextIOWrapper' object has no attribute 'writes'
# so it works as expected










