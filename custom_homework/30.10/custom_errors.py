# will just inherit functionalities of an Exception class duw to hierarchy
class MyExceptionClass(ZeroDivisionError):

    def __init__(self, message):
        self.message = message


try:
    raise MyExceptionClass("It seems you have an error!")
except MyExceptionClass as err:
    print(err)
