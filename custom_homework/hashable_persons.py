# to note that I changed pretty much the class methods
# the reason is that, for example, by using getting_older() we would allow to change the age of a person
# usually, we want this to happen :) but here, because we're practicing implementing hash dunder method
# we would erase these functionalities from all classes below
# because hash, by definition, should return each time the same encoded output
# but as we'll see, if we change, for example one parameter (age), than the value of hash will change too,
# and we don't want this behaviour
# for that reason, I will make properties (getters) for all the class' attributes (which can't be mutable),
# so they can't be overwritten


class Person:

    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        return isinstance(other, Person) and self._first_name == other._first_name\
            and self.last_name == other.last_name and self.age == other.age

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.age))

    def __str__(self):
        return f"The name of this person is {self.first_name} {self.last_name}, (s)he is {self.age} y.o"


class Student(Person):

    def __init__(self, first_name, last_name, age, years_of_study, no_of_school_subjects):
        super().__init__(first_name, last_name, age)
        self._years_of_study = years_of_study
        self._no_of_school_subjects = no_of_school_subjects

    @property
    def years_of_study(self):
        return self._first_name

    @property
    def no_of_school_subjects(self):
        return self._no_of_school_subjects

    def __eq__(self, other):
        return isinstance(other, Student) and self.first_name == other.first_name \
            and self.last_name == other.last_name and self.age == other.age \
            and self.years_of_study == other.years_of_study \
            and self.no_of_school_subjects == other.no_of_school_subjects

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.age, self.years_of_study, self.no_of_school_subjects))

    def __str__(self):
        return f"The name of this student is {self.first_name} {self.last_name}, (s)he is {self.age} y.o. " \
               f"He has {self.years_of_study} more years of study left, and he studies " \
               f"{self.no_of_school_subjects} subjects at school."


class BusDriver(Person):

    def __init__(self, first_name, last_name, age, driven_car, no_of_km_driven=0):
        super().__init__(first_name, last_name, age)
        self._driven_car = driven_car
        self._no_of_km_driven = no_of_km_driven

    @property
    def driven_car(self):
        return self._driven_car

    @property
    def no_of_km_driven(self):
        return self._no_of_km_driven

    def __eq__(self, other):
        return isinstance(other, BusDriver) and self.first_name == other.first_name \
            and self.last_name == other.last_name and self.age == other.age \
            and self.no_of_km_driven == other.no_of_km_driven \
            and self.no_of_km_driven == other.no_of_km_driven

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.age, self.driven_car, self.no_of_km_driven))

    def __str__(self):
        return f"The name of this Bus Driver is {self.first_name} {self.last_name}, (s)he is {self.age} y.o. " \
               f"(s)he currently drives a {self.driven_car} which he likes a lot, and (s)he has driven " \
               f"{self.no_of_km_driven} km so far at this job. The mileage is changing daily."


class HospitalPatient(Person):

    def __init__(self, first_name, last_name, age, family_doctor, diseases):
        super().__init__(first_name, last_name, age)
        self._family_doctor = family_doctor
        self._diseases = diseases

    @property
    def family_doctor(self):
        return self._family_doctor

    @property
    def diseases(self):
        return self._diseases

    def __eq__(self, other):
        return isinstance(other, HospitalPatient) and self.first_name == other.first_name \
            and self.last_name == other.last_name and self.age == other.age \
            and self.family_doctor == other.family_doctor \
            and self.diseases == other.diseases

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.age, self.family_doctor, self.diseases))

    def __str__(self):
        return f"The name of this Hospital Patient is {self.first_name} {self.last_name}, (s)he is {self.age} y.o. " \
               f"His/her family doctor is, at the moment, {self.family_doctor}, " \
               f"who confirmed that our patient is suffering from the following diseases: {self.diseases}."


first_student = Student("Mary", "Gomez", 16, 4, 5)
print(hash(first_student))

print("\n")

second_student = Student("Mary", "Gomez", 17, 4, 5)
print(hash(first_student) == hash(second_student))

print("\n")

my_bus_driver = BusDriver("John", "Smith", 33, "Ford", 1000)
print(hash(my_bus_driver))

print("\n")

new_patient = HospitalPatient('Erika', 'Johnson', 40, 'Mr. Mike Jenner', 'pneumonia')
print(hash(new_patient))

# now that our classes' objects are hashable we can use them as keys for dictionaries:
unique_dict = {first_student: "student",
               second_student: "new student",
               my_bus_driver: "driver",
               new_patient: "hospital"}

for key in unique_dict:
    print(key)

# output:
"""
The name of this student is Mary Gomez, (s)he is 16 y.o. He has Mary more years of study left, 
and he studies 5 subjects at school.
The name of this student is Mary Gomez, (s)he is 17 y.o. He has Mary more years of study left, 
and he studies 5 subjects at school.
The name of this Bus Driver is John Smith, (s)he is 33 y.o. (s)he currently drives a Ford which he likes a lot, 
and (s)he has driven 1000 km so far at this job. The mileage is changing daily.
The name of this Hospital Patient is Erika Johnson, (s)he is 40 y.o. His/her family doctor is, at the moment, 
Mr. Mike Jenner, who confirmed that our patient is suffering from the following diseases: pneumonia.
"""