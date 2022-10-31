import json


def load_users_from_json(job):
    with open(f"uber_{job}.json") as uber_users:
        users_data = json.load(uber_users)
    return users_data


def start_sign_up():
    user_function = ''
    while user_function not in ["d", "p"]:
        user_function = input("Are you a driver or a passenger? (d/p): ")
    if user_function == "d":
        new_driver = Driver()
        new_driver.sign_up()
    elif user_function == "p":
        new_passenger = Passenger()
        new_passenger.sign_up()


class User:

    def __init__(self):
        self.username = input("Please choose an username: ")
        self.password = ''
        # self.logged_in = False

    # def login(self):
    #     drivers_details = load_users_from_json("drivers")
    #     passengers_details = load_users_from_json("passengers")
    #     if self.username in drivers_details or self.username in passengers_details:
    #         while not self.logged_in:
    #             input_password = input("Please type your password: ")
    #             if input_password == self.password:
    #                 self.logged_in = True
    #                 print("You are logged in")
    #             else:
    #                 print("Wrong password")

    def sign_up(self):
        print("Creating your account!")
        self.password = input("Please type your new password: ")
        if self.__class__ == Driver:
            drivers_dictionary = load_users_from_json("drivers")
            drivers_dictionary.update({self.username: self.password})
            with open("uber_drivers.json", "w") as uber_users:
                json.dump(drivers_dictionary, uber_users,
                          indent=4)
        elif self.__class__ == Passenger:
            passengers_dictionary = load_users_from_json("passengers")
            passengers_dictionary.update({self.username: self.password})
            with open("uber_passengers.json", "w") as uber_users:
                json.dump(passengers_dictionary, uber_users,
                          indent=4)
        print("Now you should log in!")


class Driver(User):

    def __init__(self):
        super().__init__()


class Passenger(User):

    def __init__(self):
        super().__init__()


def new_login(username_searched, job_info):
    print("Your user exists! Let's log in!")
    logged_in = False
    while not logged_in:
        input_password = input("Please type your password: ")
        if input_password == job_info[username_searched]:
            logged_in = True
            print("You are logged in")
        else:
            print("Wrong password")


def run_application():
    drivers_info = load_users_from_json("drivers")
    passengers_info = load_users_from_json("passengers")
    if len(drivers_info) == 0 and len(passengers_info) == 0:
        print("It seems you are the first user of our app. Please sign up!")
        start_sign_up()
    else:
        print("Welcome to Uber app!")
        input_username = input("Please type your username: ")
        if input_username in drivers_info:
            new_login(input_username, drivers_info)
        elif input_username in passengers_info:
            new_login(input_username, passengers_info)
        else:
            print("Your user doesn't exist! Let's sign up!")
            start_sign_up()


run_application()

