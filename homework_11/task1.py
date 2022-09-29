class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def getting_older(self):
        self.age += 1

    def favorite_color(self, fav_color=None):
        print(f"The fav color of {self.first_name} {self.last_name} is {fav_color}")

    def __str__(self):
        return f"The name of this person is {self.first_name} {self.last_name}, (s)he is {self.age} y.o"


class Student(Person):

    def __init__(self, first_name, last_name, age, years_of_study, no_of_school_subjects):
        super().__init__(first_name, last_name, age)
        self.years_of_study = years_of_study
        self.no_of_school_subjects = no_of_school_subjects

    def years_remained(self, year_passed=1):
        if self.years_of_study == 0:
            print(f"Congrats! {self.first_name} {self.last_name} graduated!")
        else:
            self.years_of_study -= year_passed
            print(f"{self.first_name} {self.last_name} has {self.years_of_study} years of study left!")

    def __str__(self):
        return f"The name of this student is {self.first_name} {self.last_name}, (s)he is {self.age} y.o. " \
               f"He has {self.years_of_study} more years of study left, and he studies " \
               f"{self.no_of_school_subjects} subjects at school."


class Teacher(Person):

    def __init__(self, first_name, last_name, age, years_of_experience, subject_taught, salary):
        super().__init__(first_name, last_name, age)
        self.years_of_experience = years_of_experience
        self.subject_taught = subject_taught
        self.salary = salary

    def raise_of_salary(self, extra_income):
        self.salary += extra_income
        print(f"Hourray! The new salary is {self.salary}!")

    def __str__(self):
        return f"The name of this student is {self.first_name} {self.last_name}, " \
               f"(s)he is {self.age} y.o. He has {self.years_of_experience} years of teaching experience. He teaches " \
               f"{self.subject_taught} and he's proud of his {self.salary}$ salary."


first_person = Person("John", "Ross", 33)
print(first_person)
first_person.favorite_color("Blue")
first_person.getting_older()
print(f"Now he is {first_person.age} years old, he's getting older..")
print("\n")

first_student = Student("Oana", "S", 21, 3, 6)
print(first_student)
first_student.favorite_color("Green")
first_student.years_remained()          # a year of school passed
print("\n")

first_teacher = Teacher("Mike", "Alexander", 40, 18, "Physics", 2000)
print(first_teacher)
first_teacher.raise_of_salary(250)


