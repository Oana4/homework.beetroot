def calculate_power_of(base):
    def math_operation(power):
        return base ** power
    return math_operation


base_of_two = calculate_power_of(2)

print(base_of_two(5))
