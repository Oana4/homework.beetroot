from functools import wraps


def logger(func):
    @wraps(func)
    def decorated_func(*args):
        print(f"{func.__name__} called with arguments {str(args)}")
        return func(*args)
    return decorated_func


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(2, 3)
square_all(1, 2, 3)