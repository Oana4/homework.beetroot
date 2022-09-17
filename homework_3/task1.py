my_string = input('Choose a string, please: ')

if len(my_string) < 2:
    print('Empty String')
else:
    print(my_string[:2] + my_string[-2] + my_string[-1])
