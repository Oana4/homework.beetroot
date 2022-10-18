# Create a class Person that’ll take two arguments “name” and “surname”. And create a method “get_full_name”
# which will return to you - the full name of this special instance. Advanced:
# transform a method into a property that’ll be named “full_name”.
# You'll need - https://www.geeksforgeeks.org/python-property-decorator-property/ , for advanced level.

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def get_full_name(self):
#         return self.name + self.surname
#
#
# person1 = Person("Rita", " S")
#
# print(person1.get_full_name())


# advanced:

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + self.surname


person1 = Person("Oana", " S")

print(person1.full_name)
