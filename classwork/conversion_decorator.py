# You need to transform the results of some function from a str type to an int type.
# Create a decorator for it. Advanced: create params for the decorator which will allow you to specify the final type.

def str_to_int(type_):
    def str_to_int_dec(func):
        def wraps(*args):
            try:
                return type_(func(*args))
            except TypeError as err:
                print(err)
        return wraps
    return str_to_int_dec


@str_to_int(int)
def test():
    return "22"


print(type(test()), test())

