class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", "a") as log_file:
            log_file.write(f"{msg} \n")


class MyExceptionClass(RecursionError):
    pass


try:
    raise CustomException("You will find this error in the logs.txt file :)")
except CustomException as my_err:
    print(my_err)

