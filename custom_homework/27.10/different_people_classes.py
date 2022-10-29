class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def getting_older(self):
        self.age += 1

    def __str__(self):
        return f"The name of this person is {self.first_name} {self.last_name}, (s)he is {self.age} y.o"


class Student(Person):

    def __init__(self, first_name, last_name, age, years_of_study, no_of_school_subjects):
        super().__init__(first_name, last_name, age)
        self.years_of_study = years_of_study
        self.no_of_school_subjects = no_of_school_subjects

    def year_passed(self, an_year_passed=1):
        if self.years_of_study == 0:
            print(f"Congrats! {self.first_name} {self.last_name} graduated!")
        else:
            self.years_of_study -= an_year_passed
            print(f"{self.first_name} {self.last_name} has {self.years_of_study} years of study left!")

    def enrolled_to_course(self, subject_name):
        self.no_of_school_subjects += 1
        print(f"{self.first_name} {self.last_name} enrolled to another school course, namely {subject_name}!")

    def __str__(self):
        return f"The name of this student is {self.first_name} {self.last_name}, (s)he is {self.age} y.o. " \
               f"He has {self.years_of_study} more years of study left, and he studies " \
               f"{self.no_of_school_subjects} subjects at school."


class BusDriver(Person):

    def __init__(self, first_name, last_name, age, driven_car, no_of_km_driven=0):
        super().__init__(first_name, last_name, age)
        self.driven_car = driven_car
        self.no_of_km_driven = no_of_km_driven

    def add_km(self, more_km):
        self.no_of_km_driven += more_km
        print(f"After today's routes, our bus driver added {more_km} more kilometres at his car's mileage.")

    def change_his_bus(self, new_bus):
        self.driven_car = new_bus
        print(f"Our bus driver changed his car! Now he drives a {new_bus}!")

    def __str__(self):
        return f"The name of this Bus Driver is {self.first_name} {self.last_name}, (s)he is {self.age} y.o. " \
               f"(s)he currently drives a {self.driven_car} which he likes a lot, and (s)he has driven " \
               f"{self.no_of_km_driven} km so far at this job. The mileage is changing daily."


class HospitalPatient(Person):

    def __init__(self, first_name, last_name, age, family_doctor, diseases: list):
        super().__init__(first_name, last_name, age)
        self.family_doctor = family_doctor
        self.diseases = diseases

    def change_family_doctor(self, new_family_doctor):
        self.family_doctor = new_family_doctor
        print(f"New family doctor for {self.first_name} {self.last_name}. Name: {new_family_doctor}")

    def add_new_disease(self, new_disease):
        self.diseases.append(new_disease)
        print(f"Sad news! We found out {self.first_name} {self.last_name} also suffers from {new_disease}!")

    def __str__(self):
        return f"The name of this Hospital Patient is {self.first_name} {self.last_name}, (s)he is {self.age} y.o. " \
               f"His/her family doctor is, at the moment, {self.family_doctor}, " \
               f"who confirmed that our patient is suffering from the following diseases: {self.diseases}."

