phone_num = input('Please insert your phone number, in a format of 10 digits: ')

if len(phone_num) == 10 and phone_num.isdigit():
    print('Correct! Your phone number is added!')
else:
    print('Wrong syntax!')