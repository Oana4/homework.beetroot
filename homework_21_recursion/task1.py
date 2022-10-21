# Returns  x ^ exp
def to_power(x, exp):
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    elif exp == 0:
        return 1
    else:
        return x * to_power(x, exp - 1)


assert to_power(2, 3) == 8

assert to_power(3.5, 2) == 12.25

# assert to_power(2, -1) == ValueError("This function works only with exp > 0.")
