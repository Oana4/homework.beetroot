def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


class Mathematician:

    def filter_leaps(self, list_of_years):
        return [year for year in list_of_years if is_leap_year(year)]

    def remove_positives(self, list_of_int):
        return [num for num in list_of_int if num < 0]

    def square_nums(self, list_of_squares):
        return [square**2 for square in list_of_squares]


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))                     # == [49, 121, 25, 16]
print(m.remove_positives([26, -11, -8, 13, -90]))       # == [-11, -8, -90]
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))   # == [1884, 2020]

