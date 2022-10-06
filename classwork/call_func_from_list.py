# Create two functions. One print “Hi”, second print “Goodbye”.
# Put them both into a list. Now, if the user will input 1 - you must fire the first function.
# If he’ll input 2 - you must fire a second one.

question = input("Press 0 for Hi and 1 for goodbye\n")


def hi_there():
    print("HI")


def goodbye():
    print("Bye")


functions = [hi_there, goodbye]
try:
    functions[int(question)]()
except:
    print('You did something wrong')