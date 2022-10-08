# You need a validation decorator, which will raise a Value error if one of the params of the function -
# will not be a string type. Advanced: add a parameter to decorator “searching_str”,
# this string must be in at least one argument of the wrapped function, or you should raise an error.

def search_param(searching_str):
    def validation_decorator(func):
        def wrapper(*args):
            if any(type(arg) != str for arg in args):
                raise ValueError("Not all your args are strings!")
            assert searching_str in args, "The searched string not in args!"
            return func(*args)
        return wrapper
    return validation_decorator


@search_param("bat")
def test_func(a, b):
    return a + b


test_func('my', 'cat')
# test_func(2, 'cat')


