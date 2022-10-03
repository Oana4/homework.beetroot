# Some nice theory:
# Code objects are simply looks into the different aspects of a compiled function.
# A code object describes different aspects of a function, based on its byte code.
# Every function in Python has a __code__ attribute that holds its code object.
# co_nlocals — is the number of local variables used by the function (including arguments).


def main_function():
    first_var = "Hello"
    second_var = "my name is"
    third_var = "Oana"
    fourth_var = ":)"

    return first_var + second_var + third_var + fourth_var


def count_func_variables(any_function):
    return any_function.__code__.co_nlocals


print(count_func_variables(main_function))