# will just inherit functionalities of an Exception class due to hierarchy
class SpecificZeroDivException(ZeroDivisionError):

    def __init__(self, message):
        self.message = message


try:
    raise ZeroDivisionError("Your numerator can't be 0!")
except ZeroDivisionError:
    raise SpecificZeroDivException("This is a child of ZeroDivisionError called :)")
