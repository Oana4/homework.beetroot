import sys

print(sys.path)

# 1st question: is it possible to change sys.path from within Python
# if now is /home/oana/PycharmProjects/homework@beetroot
# I'll also add another Pycharm Project that contains a code so that it'll be available
sys.path.append("/home/oana/PycharmProjects/pythonProject/main.py")
print(sys.path)
# so the answer is yes, we can change the sys.path from our program

# 2nd question: does it affect where Python looks for module files?
# my answer: it still keeps all the directories that it was designed to look into,
# we can only add new ones, so yes, we can say it 'affects' its searching by having more options

# another way to do the above thing:
PYTHONPATH = "/home/oana/PycharmProjects/pythonProject/main.py"
print(sys.path)
# I obtained the same result
