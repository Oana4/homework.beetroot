# Password Generator
#     1.    Password length should be from 4 to 16 symbols
#     2.    The following options should be available for the user:
# -  latin alphabet, upper case letters, lower case letters, punctuation symbols
# the response can be Y/N (possible usage y/n and Y/N)
#     3. Based on the given bass the password is generated randomly and given to the user

from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def users_choice():
    password_alphabet = ''
    answers = set()
    ascii_option = [ascii_lowercase, ascii_uppercase, digits, punctuation]
    string_option = ['lowercase letters', 'uppercase letters', 'digits', 'punctuation']
    while len(answers) == 0 or (len(answers) == 1 and 'n' in answers):
        print("You must have some preferences for password's symbols. Let's see what you choose!")
        for ascii_item, string_item in zip(ascii_option, string_option):
            while True:
                users_answer = input(f'Do you want to use {string_item}? (y/n): ')
                if users_answer == 'y':
                    password_alphabet += ascii_item
                    answers.add('y')
                    break
                elif users_answer == 'n':
                    answers.add('n')
                    break
                else:
                    print('Please type y or n! :(')
    return password_alphabet


def password_generator():
    length = 0
    while not 4 <= length <= 16:
        length = input('How long do you want the password to be? (4 - 16 characters): ')
        if length.isdigit():
            length = int(length)
        else:
            length = 0

    final_alphabet = users_choice()

    password = ''.join(choices(final_alphabet, k=length))
    print("Your new generated password is: \n", password)


password_generator()
