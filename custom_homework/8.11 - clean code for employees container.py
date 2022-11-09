from datetime import datetime


class Employee:
    def __init__(self, name, age, position, salary_per_hour):
        self.name = name
        self.age = age
        self.position = position
        self.salary_per_hour = salary_per_hour
        self.hours_worked = 0
        self.started_pass = 0

    def __repr__(self):
        return f"Name: {self.name}, hourly salary: {self.salary_per_hour}"

    def start_working(self):
        self.started_pass = datetime.now()

    def finish_working(self):
        if self.started_pass != 0:
            difference = datetime.now() - self.started_pass
            self.hours_worked += difference.total_seconds() / 3600
            self.started_pass = 0

    def calculate_salary(self):
        return self.hours_worked * self.salary_per_hour


class ListOfEmployees:
    list_of_employees = []

    @classmethod
    def add_employee(cls):
        name = input("What is your employee's name? ")
        age = int(input("What is your employee's age? "))
        position = input("What is your employee's position? ")
        salary_per_hour = float(input("What is your employee's hourly salary? "))

        new_employee = Employee(name, age, position, salary_per_hour)
        cls.list_of_employees.append(new_employee)
        return new_employee

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.list_of_employees):
            temp_index = self.index
            self.index += 1
            return self.list_of_employees[temp_index]
        else:
            raise StopIteration


e1 = ListOfEmployees.add_employee()
e1.start_working()
e1.finish_working()
print(e1.calculate_salary())

print(ListOfEmployees.list_of_employees)