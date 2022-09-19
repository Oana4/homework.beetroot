def make_operation(operator, *numbers):
    if operator == '+':
        return sum(numbers)
    elif operator == '-':
        difference = numbers[0]
        for number in numbers[1:]:
            difference -= number
        return difference
    elif operator == '*':
        product = 1
        for number in numbers:
            product *= number
        return product
    else:
        print('Maybe operator is not known')


# some test to check function
operation_result = make_operation('-', 2, 3, 4)
print(operation_result)

