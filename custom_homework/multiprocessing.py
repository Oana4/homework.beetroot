# Create your non-concurrent solution, and both multithreading and multiprocessing solutions for the problem below.
# Measure time of execution for all solutions and draw conclusions on what's the most efficient approach for your task.

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
import threading
import multiprocessing

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

# @timer
# def repeat_func_with_processes(num_of_reps, limit):
#     p = multiprocessing.Pool()

if __name__ == '__main__':
    repeat_func(5, 1000)
    repeat_func_with_threads(5, 1000)