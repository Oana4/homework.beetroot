class Dog:

    age_factor = 7

    def __init__(self, name, dog_age):
        self.name = name
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor


tucker = Dog("Tucker", 2)
print(f"In human years, {tucker.name} is: {tucker.human_age()} years old.")