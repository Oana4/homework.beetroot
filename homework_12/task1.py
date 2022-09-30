def animal_talks(favorite_animal):
    favorite_animal.talk()


class Animal:

    def talk(self):
        raise NotImplementedError("This method should be used by subclasses.")


class Dog(Animal):

    def talk(self):
        print("woof woof")


class Cat(Animal):

    def talk(self):
        print("meow")


tucker = Dog()
giulietta = Cat()

animal_talks(tucker)
animal_talks(giulietta)

