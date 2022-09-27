# User could input to you something. You'll to transform it to int and divide 1 by this number.
# Don't use if/else blocks and print "Wrong input" in case if some exception happen

user_input = input("Please try to input an integer: ")

try:
    1 / int(user_input)
except (ZeroDivisionError, ValueError):
    print("Wrong input")
    