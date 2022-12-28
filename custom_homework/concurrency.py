# Create your non-concurrent solution, and both multithreading and multiprocessing solutions for the problem below.
# Measure time of execution for all solutions and draw conclusions on what's the most efficient approach for your task.

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
import threading
import multiprocessing
import time


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

def is_prime(number):
    a = 2
    while a <= math.sqrt(number):
        if number % a == 0:
            return False
        a = a + 1
    return True

def sum_of_primes(limit):
    total_sum = 2
    for i in range(3, limit+1, 2): # I will just skip the even numbers because we know for sure they are not prime
        if is_prime(i):
            total_sum += i
    return total_sum

@timer
def repeat_func(num_of_reps, limit):
    for i in range(num_of_reps):
        sum_of_primes(limit)

@timer
def repeat_func_with_threads(num_of_reps, limit):
    for i in range(num_of_reps):
        obj = threading.Thread(target=sum_of_primes, args=(limit,))
        obj.start()
        obj.join()

@timer
def repeat_func_with_processes(num_of_reps, limit):
    for i in range(num_of_reps):
        p = multiprocessing.Process(target=sum_of_primes, args=(limit,))
        p.start()
        p.join()

# if __name__ == '__main__':
#     # By doing this:
#     repeat_func(2, 2000000)
#     repeat_func_with_threads(2, 2000000)
#     repeat_func_with_processes(2, 2000000)
#     # I obtained the following results:
#     # repeat_func took 43.96636424s to execute
#     # repeat_func_with_threads took 43.57954469s to execute
#     # repeat_func_with_processes took 43.46427336s to execute
#
#     # Which I, personally, was expecting, because for the multiprocess part, for example
#     # the tasks weren't divided
#     # for this, each function waited for the previous one in order to be executed
#     # now I want to try to use multiprocessing on dividing their execution

if __name__ == "__main__":
    start_time = time.perf_counter()
    p1 = multiprocessing.Process(target=repeat_func, args=(2, 2000000))
    p2 = multiprocessing.Process(target=repeat_func_with_threads, args=(2, 2000000))
    p3 = multiprocessing.Process(target=repeat_func_with_processes, args=(2, 2000000))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    end_time = time.perf_counter()
    print(f"This entire program execution is {end_time-start_time}, "
          f"compared to the 3*43 = 129s to the previous approach")
    # This time, my result is the following:
    # repeat_func_with_threads took 51.13362034s to execute
    # repeat_func_with_processes took 51.79584890s to execute
    # repeat_func took 51.88108879s to execute
    # This entire program execution is 51.8835383859996, compared to the 3*43 = 129s to the previous approach

    # So I used as many processors as needed and all the work was shared and only now I can see the actual difference
    # and also improvements that come with multiprocessing! The new time is almost only one third from the previous'
    # approach time of execution, so it's awesome!! :)