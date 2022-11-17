import sqlite3
from custom_homework.different_people_27_10.different_people_classes import Person, BusDriver, Student, HospitalPatient

conn = sqlite3.connect("people.db")

c = conn.cursor()


# c.execute("""CREATE TABLE drivers (
#             first_name text,
#             last_name text,
#             age integer,
#             driven_car text,
#             km_driven integer
#             )""")

# c.execute("INSERT INTO drivers VALUES ('John', 'Michael', 33, 'Ford', 100)")
# conn.commit()
#
# c.execute("SELECT * FROM drivers")
# print(c.fetchall())

# c.execute("""CREATE TABLE students (
#             first_name text,
#             last_name text,
#             age integer,
#             years_of_study integer,
#             no_of_school_subjects integer
#             )""")

# c.execute("""CREATE TABLE patients (
#             first_name text,
#             last_name text,
#             age integer,
#             family_doctor text,
#             new_disease text
#             )""")


# Drivers Table
def add_new_driver(new_driver):
    with conn:
        c.execute("INSERT INTO drivers VALUES (:first, :last, :age, :driven_car, :km_driven)",
                  {'first': new_driver.first_name,
                   'last': new_driver.last_name,
                   'age': new_driver.age,
                   'driven_car': new_driver.driven_car,
                   'km_driven': new_driver.no_of_km_driven})


def change_drivers_bus(driver, new_car_brand):
    with conn:
        c.execute("""UPDATE drivers SET driven_car = :new_bus
                     WHERE first_name = :first AND last_name = :last""",
                  {'first': driver.first_name, 'last': driver.last_name, 'new_bus': new_car_brand})


def remove_driver_by_name(first_name, last_name):
    with conn:
        c.execute("DELETE FROM drivers WHERE first_name = :first AND last_name = :last",
                  {'last': last_name, 'first': first_name})


def get_all_drivers():
    c.execute("SELECT * FROM drivers")
    return c.fetchall()


# Students Table
def add_new_student(new_student):
    with conn:
        c.execute("INSERT INTO students VALUES (:first, :last, :age, :years_of_study, :no_of_school_subjects)",
                  {'first': new_student.first_name,
                   'last': new_student.last_name,
                   'age': new_student.age,
                   'years_of_study': new_student.years_of_study,
                   'no_of_school_subjects': new_student.no_of_school_subjects})


def remove_student_by_name(first_name, last_name):
    with conn:
        c.execute("DELETE FROM students WHERE first_name = :first AND last_name = :last",
                  {'last': last_name, 'first': first_name})


def get_students_by_last_name(last):
    c.execute("SELECT * FROM students WHERE last_name=:last_name", {'last_name': last})
    return c.fetchall()


# Patients table
def add_new_patient(new_patient):
    with conn:
        c.execute("INSERT INTO patients VALUES (:first, :last, :age, :family_doctor, :new_disease)",
                  {'first': new_patient.first_name,
                   'last': new_patient.last_name,
                   'age': new_patient.age,
                   'family_doctor': new_patient.family_doctor,
                   'new_disease': new_patient.diseases})


def change_family_doctor(patient, new_doctor):
    with conn:
        c.execute("""UPDATE patients SET family_doctor = :fam_doc
                     WHERE first_name = :first AND last_name = :last""",
                  {'first': patient.first_name, 'last': patient.last_name, 'fam_doc': new_doctor})


def remove_patient_by_name(first_name, last_name):
    with conn:
        c.execute("DELETE FROM patients WHERE first_name = :first AND last_name = :last",
                  {'last': last_name, 'first': first_name})


def get_patients_by_family_doc(family_doc):
    c.execute("SELECT * FROM patients WHERE family_doctor=:family_doctor", {'family_doctor': family_doc})
    return c.fetchall()


first_student = Student("Mary", "Gomez", 16, 4, 5)
second_student = Student("Selena", "Gomez", 15, 5, 7)
third_student = Student("Kate", "Eve", 17, 3, 4)
my_bus_driver = BusDriver("John", "Smith", 33, "Ford", 1000)
first_patient = HospitalPatient('Erika', 'Johnson', 40, 'Mr. Mike Jenner', 'pneumonia')

add_new_student(first_student)
add_new_student(second_student)
add_new_student(third_student)
add_new_driver(my_bus_driver)
add_new_patient(first_patient)

list_of_drivers = get_all_drivers()
print(list_of_drivers)

gomez_students = get_students_by_last_name('Gomez')
print(gomez_students)

at_family_doc = get_patients_by_family_doc('Mr. Mike Jenner')
print(at_family_doc)

remove_student_by_name("Selena", "Gomez")
gomez_students = get_students_by_last_name('Gomez')
print(gomez_students)

conn.close()
