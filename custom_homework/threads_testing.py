import threading


def timer(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute

    return inner


def factorial(x):
    if x in [0, 1]:
        return 1
    elif x < 0:
        return None
    else:
        return x * factorial(x - 1)


@timer
def repeat_factorial(num_of_reps, x):
    for i in range(num_of_reps):
        factorial(x)


@timer
def repeat_factorial_with_threads(num_of_reps, x):
    for i in range(num_of_reps):
        obj = threading.Thread(target=factorial, args=(x,))
        obj.start()
        obj.join()


if __name__ == '__main__':
    repeat_factorial(22, 10)
    repeat_factorial_with_threads(22, 10)

# Here I'll leave my output
# repeat_factorial took 0.00002362s to execute
# repeat_factorial_with_threads took 0.00139305s to execute
# So the threads one is taking much more time than the simple & old one