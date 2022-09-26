import os
import json

current_directory = os.curdir
files_in_current_dir = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]

if "phonebook.json" in files_in_current_dir:
    with open('phonebook.json') as f:
        phonebook = json.load(f)

    dict_of_actions = {
        1: 'add a new record',
        2: 'search by first name',
        3: 'search by last name',
        4: 'search by full name',
        5: 'search by telephone number',
        6: 'search by city/state',
        7: 'delete a record for a phone number',
        8: 'update a record for a phone number',
        9: 'exit'
    }

    # allows user to make modifications
    user_command = input(f"Please choose your action by entering the corresponding number: \n{dict_of_actions}: ")

    # create functions which help us handle the phonebook


    def add_user():
        new_user = {"First name": input("First name: "),
                    "Last name": input("Last name: "),
                    "Phone number": input("Phone number: "),
                    "City/State": input("City/State: ")}
        phonebook.append(new_user)


    def delete_user(old_member):
        phonebook.remove(old_member)


    def search_by(users_key, users_value):
        if len(phonebook) == 0:
            print("The phonebook doesn't have any records!")
        else:
            for member in phonebook:
                if member[users_key] == users_value:
                    print("Your member exists! Here are his details: ")
                    for key, value in member.items():
                        print(f"{key} : {value}")
                else:
                    print("Your member hasn't been found, sorry :(")


    def search_full_name():
        full_name = input("Please type the full name that you want to find: ").split()
        for member in phonebook:
            if member["First name"] == full_name[0] and member["Last name"] == full_name[1]:
                print("Your member exists! Here are his details: ")
                for key, value in member.items():
                    print(f"{key} : {value}")
            else:
                print("Your member hasn't been found, sorry :(")


    def delete_record():
        member_to_be_deleted = input("Please type the associated phone number of the user that you want to delete: ")
        for member in phonebook:
            if member["Phone number"] == member_to_be_deleted:
                print("Your member exists! His details will be deleted!")
                phonebook.remove(member)
            else:
                print("Your member hasn't been found, sorry :( Try again, please")


    def update_record():
        member_to_be_updated = input("Please type the associated phone number of the user that you want to update: ")
        key_to_be_updated = input("Please type the detail of the user that you want to update: ")
        for member in phonebook:
            if member["Phone number"] == member_to_be_updated:
                member[key_to_be_updated] = input("Please update the detail that you've chosen.")


    while True:

        if user_command == '1':
            add_user()
            print("The new phonebook is: ", phonebook)

        if user_command == '2':
            member_first_name = input("Please type the first name that you want to find: ")
            search_by("First name", member_first_name)

        if user_command == '3':
            member_last_name = input("Please type the last name that you want to find: ")
            search_by("Last name", member_last_name)

        if user_command == '4':
            search_full_name()

        if user_command == '5':
            phone_number = input("Please type the phone number that you want to find: ")
            search_by("Phone number", phone_number)

        if user_command == '6':
            city_state = input("Please type the city/state that you want to find: ")
            search_by("City/State", city_state)

        if user_command == '7':
            delete_record()
            print("The new phonebook is: \n", phonebook)

        if user_command == '8':
            update_record()
            print("The new phonebook is: \n", phonebook)

        if user_command == '9':
            with open('phonebook.json', 'w') as f:
                json.dump(phonebook, f)
            break

        print('\n')
        user_command = input(f"Please choose your action by entering the corresponding number: \n{dict_of_actions}: ")
else:
    print("Your json file doesn't exist!")
