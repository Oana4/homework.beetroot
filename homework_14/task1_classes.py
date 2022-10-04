class Logger:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        print(f"{self.function.__name__} called with arguments:", args)
        # self.function(args)


@Logger
def add(x, y):
    return x + y


@Logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(2, 3)
square_all(1, 2, 3)