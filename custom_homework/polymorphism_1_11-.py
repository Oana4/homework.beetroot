# this should be treated more like a scientific app (regarding its functionalities)
class Galaxy:

    def __init__(self, galaxy_name, galaxy_age, galaxy_mass):
        self.galaxy_name = galaxy_name
        self.galaxy_age = galaxy_age
        self.galaxy_mass = galaxy_mass

    @staticmethod
    def comparison(first_obj, second_obj, operator):
        if not isinstance(second_obj, Galaxy):
            raise NotImplementedError("Can't compare 2 objects from 2 different classes!")
        criteria_of_comparison = ''
        while criteria_of_comparison not in ['age', 'mass']:
            criteria_of_comparison = input("Please choose your comparison criteria (age or mass): ")
        if criteria_of_comparison == 'age':
            return eval(f'{first_obj.galaxy_age} {operator} {second_obj.galaxy_age}')
        elif criteria_of_comparison == 'mass':
            return eval(f'{first_obj.galaxy_mass} {operator} {second_obj.galaxy_mass}')

    def __lt__(self, other):
        return self.comparison(self, other, "<")

    def __le__(self, other):
        return self.comparison(self, other, "<=")

    def __eq__(self, other):
        return self.comparison(self, other, "==")

    def __ne__(self, other):
        return self.comparison(self, other, "!=")

    def __gt__(self, other):
        return self.comparison(self, other, ">")

    def __ge__(self, other):
        return self.comparison(self, other, ">=")


galaxy_1 = Galaxy("Milky Way", 1.361e10, 1.5e12)
galaxy_2 = Galaxy("Andromeda", 1.001e10, 8e11)
not_a_galaxy = 3
print(galaxy_1 >= galaxy_2)
print(galaxy_1 == galaxy_2)
print(galaxy_1 != galaxy_2)
print(galaxy_1 < galaxy_2)
print(galaxy_1 < not_a_galaxy)

