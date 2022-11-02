from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_type(_type):
        def inner_to_type(func):
            @wraps(func)
            def decorator_to_type(*args):
                try:
                    return _type(func(*args))
                except ValueError(f"The result cannot be converted to {_type}") as err:
                    print(err)
            return decorator_to_type
        return inner_to_type


@TypeDecorators.to_type(int)
def do_nothing(string: str):
    return string


@TypeDecorators.to_type(bool)
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
