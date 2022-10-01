from math import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError("Denominator can't be 0!")

    def reduce_by_common_div(self, numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        return Fraction(int(numerator / common_divisor), int(denominator / common_divisor))

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return self.reduce_by_common_div(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return self.reduce_by_common_div(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return self.reduce_by_common_div(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return self.reduce_by_common_div(new_numerator, new_denominator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


x = Fraction(-3, 2)
y = Fraction(1, 4)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
