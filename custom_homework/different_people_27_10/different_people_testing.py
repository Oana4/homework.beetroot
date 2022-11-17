from different_people_classes import Student, BusDriver, HospitalPatient


first_student = Student("Mary", "Gomez", 16, 4, 5)
print(first_student)
first_student.getting_older()
print(first_student.age)
first_student.year_passed()
first_student.enrolled_to_course('Romanian Grammar')
print(first_student.no_of_school_subjects)

print("\n")

my_bus_driver = BusDriver("John", "Smith", 33, "Ford", 1000)
print(my_bus_driver)
my_bus_driver.add_km(100)
my_bus_driver.change_his_bus("Toyota")
print(my_bus_driver)

print("\n")

new_patient = HospitalPatient('Erika', 'Johnson', 40, 'Mr. Mike Jenner', ['pneumonia'])
new_patient.add_new_disease('tonsillitis')
new_patient.change_family_doctor('Mrs. Emma Sheeran')
new_patient.getting_older()
print(new_patient)
