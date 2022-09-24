# first task
with open('myfile.txt', 'w') as my_file:
    my_file.write("Hello file world!")

# second task
with open('myfile.txt') as my_file:
    print(my_file.read())

