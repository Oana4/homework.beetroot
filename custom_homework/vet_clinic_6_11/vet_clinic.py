from datetime import datetime, timedelta


class Animal:

    list_of_animals = []

    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age
        self._vaccinated = None
        self.list_of_animals.append(self)

    def __str__(self):
        return 'This is a {} named {} {} years old'.format(
            self.kind,
            self.name,
            self.age)

    def __repr__(self):
        return 'Animal("{}", "{}", {})'.format(
            self.kind,
            self.name,
            self.age)

    @classmethod
    def dog(cls):
        name = input('Your dog name is ')
        age = input('How old is it? ')
        size = input('Size of your dog: ')
        dog = cls('dog', name, age)
        dog.size = size
        return dog

    @staticmethod
    def year_ago():
        return datetime.now() - timedelta(days=365)

    @staticmethod
    def two_years_ago():
        return datetime.now() - timedelta(days=730.5)

    @property
    def vaccinated(self):
        return self._vaccinated

    def get_vaccinated(self):
        if self.kind in ['dog', 'cat']:
            if getattr(self, 'vaccination_date', self.two_years_ago()) < self.year_ago():
                self.vaccination_date = datetime.now()
                self._vaccinated = True
        else:
            self._vaccinated = False
            print("We will not vaccinate your animal!")

    @classmethod
    def get_animals_treated(cls):
        if len(cls.list_of_animals) == 0:
            print("No animals visited our clinic so far")
        else:
            for animal in cls.list_of_animals:
                print(animal)


if __name__ == '__main__':
    the_dog = Animal.dog()
    print(the_dog, the_dog.size)
    the_dog.get_vaccinated()
    print(the_dog.vaccinated)

    the_humster = Animal('humster', 'Mike', 2)
    print(the_humster)
    the_humster.get_vaccinated()
    print(the_humster.vaccinated)

    my_dog = Animal.dog()
    # user input goes here, and finally we have a dog object
    my_dog.vaccinated = True  # now our dog counts as vaccinated, but it didn't get any dose of vaccine yet!
    print(my_dog.vaccinated)

    print(Animal.get_animals_treated())
