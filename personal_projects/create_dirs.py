# let's assume that we will have 10 files with 10^9 events (each)
# we want to merge them into a bigger file, after moving each root file that's been generated into a different dir
# I'll write a template code

import os

# current_dir = os.getcwd()
new_path = "/home/oana/test_code"      # this should be the path in which I want to move those root files


# loop code for creating 10 brand-new directories
for i in range(10):                                     # make that loop with 10 iterations
    directory = f"root_data{i}"                        # create a new directory name
    specific_path = os.path.join(new_path, directory)   # create the path for the new directory
    try:
        os.makedirs(specific_path)                      # actually make the directory there
    except OSError as err:
        print(err)
