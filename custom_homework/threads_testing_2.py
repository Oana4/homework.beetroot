import threading
import requests

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


def make_request():
    response = requests.get('http://python.org')
    return response.status_code

@timer
def repeat_making_requests(num_of_reps):
    for i in range(num_of_reps):
        make_request()


@timer
def repeat_requests_with_threads(num_of_reps):
    for i in range(num_of_reps):
        obj = threading.Thread(target=make_request, args=())
        obj.start()
        obj.join()


if __name__ == '__main__':
    repeat_making_requests(10)
    repeat_requests_with_threads(10)


# This time, my output is the following:
# repeat_making_requests took 17.43910244s to execute
# repeat_requests_with_threads took 15.73362027s to execute

# So this time, finally, threads win. My theory here is that
# when using only our computer resources (as it happened with the factorial function)
# we don't see a significant difference of performance between classical way and threading way
# but when we had to access a different server and therefore to wait for it to answer, thread may
# come in really handy