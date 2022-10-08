# 1. You need to log the results of function sum(a, b) and function power(a, b) - to a file.
# + Log each time when this function calls - another file, with a timestamp. Make a decorator for this one.
# Advanced: add parameters for a decorator, which will allow you to specify the names of a file.

from datetime import datetime


def logger_to_file(time_file_name, results_file_name):
    def logger_decorator(func):
        def wraps(*args):
            result = func(*args)
            with open(time_file_name, 'a') as time_file:
                time_file.write(f'{func.__name__}: {datetime.now()}\n')
            with open(results_file_name, 'a') as result_file:
                result_file.write(f'{func.__name__}({args}): {result}\n')
            return result

        return wraps

    return logger_decorator


@logger_to_file('time_sum.txt', 'results_sum.txt')
def sum_(a, b):
    return a + b


@logger_to_file('time_pow.txt', 'results_pow.txt')
def pow_(a, b):
    return a ** b
