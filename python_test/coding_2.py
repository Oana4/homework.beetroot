from time import time


def get_time_of_execution(any_func):
    def wrap_function(*args):
        start_time = time()
        any_func(*args)
        print("The execution time is ", time() - start_time)
        return any_func(*args)
    return wrap_function


# first way
@get_time_of_execution
def calculate_factorial(num):
    factorial = 1
    for number in range(1, num + 1):
        factorial *= number
    return factorial


print(calculate_factorial(5))

# recursive way, assuming another num is a positive integer
# def factorial_func(another_num):
#     if another_num == 1:
#         return 1
#     return another_num * factorial_func(another_num-1)


# print(factorial_func(4))
