# Create a function where will be needed as an argument string_a and number_b.
# With using assert - be sure, that user input arguments of this types. After it concatenate string_a with number_b

def special_function(string_a, number_b):
    assert isinstance(string_a, str), "any string"
    assert isinstance(number_b, int), "second arg"

    return string_a + str(number_b)

# print(isinstance(True, int))
# print(type(True) == int)


print(special_function("string", "second"))
