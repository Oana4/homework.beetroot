import logging


class OpenFile(object):

    counter = 0

    def __init__(self, file_name, action_method):
        self.file = open(file_name, action_method)

    @classmethod
    def get_no_of_initialisations(cls):
        return cls.counter

    def __enter__(self):
        OpenFile.counter += 1
        return self.file

    def __exit__(self, err_type, err_value, err_traceback):
        # adding logging functionality to handle exceptions
        if err_type is not None:
            logging.exception("An exception has occurred")
        self.file.close()
        # print(self.file.closed)


with OpenFile('test.txt', 'w') as opened_file:
    opened_file.write("this is a test file")

print(f"The OpenFile class was used {OpenFile.get_no_of_initialisations()} times.")
