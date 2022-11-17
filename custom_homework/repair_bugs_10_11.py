from time import time


class Employee:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.start_time = 0
        self.end_time = 0
        self.total_hours = 0
        self.salary = 0

    def start_working(self):
        self.start_time = time()
        print("Welcome to work!")

    def end_working(self):
        self.end_time = time()
        self.total_hours += (self.end_time - self.start_time) / 3600
        print(f"Finished work for today: {self.end_time}")
        self.salary += self.total_hours * 20

    def __repr__(self):
        return f"Name: {self.name}, age: {self.age}, total hours: {self.total_hours}"


class ListOfEmployees:

    list_of_employees = []

    @classmethod
    def add_employee(cls, employee):
        cls.list_of_employees.append(employee)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.list_of_employees):
            temp_index = self.index
            self.index += 1
            return self.list_of_employees[temp_index]
        else:
            raise StopIteration()


print(ListOfEmployees.list_of_employees)
new_emp = Employee('me', 21, 'f')
ListOfEmployees.add_employee(new_emp)
new_emp.start_working()
new_emp.end_working()
print(new_emp.total_hours)
print(new_emp.salary)
print(ListOfEmployees.list_of_employees)
