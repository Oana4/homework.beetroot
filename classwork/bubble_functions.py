# Create a function_a, function_b, which calls function_a, and function_c,
# which calls function_b, and function_d
# which call function_c. Now, you'll need to bubble some information from function b into function a.
# Try to use exceptions for it

def function_a():
    raise IndexError({1, 2, 3})


def function_b():
    function_a()
    print('Another smth')


def function_c():
    print('Smth')
    function_b()


def function_d():
    try:
        function_c()
    except IndexError as e:
        print('No more error', e.args[0])


function_d()
