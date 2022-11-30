import os

mother_folder = '/home/oana/PycharmProjects/homework@beetroot'


def recursive_file_printer(the_path, space=''):
    for folder_name in os.listdir(the_path):
        print(space + folder_name)
        if os.path.isdir(os.path.join(the_path, folder_name)):
            more_space = space + "  "
            recursive_file_printer(os.path.join(the_path, folder_name), more_space)


recursive_file_printer(mother_folder)
