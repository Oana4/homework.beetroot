#!/usr/bin/env python3

# let's assume that we will have 10 dirs with 10^9 events (each)
# we want to merge them into a bigger file, after moving each root file that's been generated into a different dir
# I'll write a template code part 2

import os
import shutil
import multiprocessing

no_of_cores = multiprocessing.cpu_count()
old_path = "/home/oana/fake_root"  # this should take the path in which MNT code generates root files with data
new_path = "/home/oana/test_code"  # this should be the path in which I want to move those root files
root_files = [file for file in os.listdir(old_path)
              if '.root' in file.lower()]  # list of root files existing in old_path

break_out = False
for file in root_files:
    for i in range(10):
        if len(os.listdir(f"{new_path}/root_data_9")) == no_of_cores:
            break_out = True
            break
        if len(os.listdir(f"{new_path}/root_data_{i}")) < no_of_cores:
            shutil.move(f"{old_path}/{file}", f"{new_path}/root_data_{i}")
            break
        root_files = [file for file in os.listdir(old_path) if '.root' in file.lower()]
    if break_out:
        break

# this is a for loop to create a list with the names of the files
# existing in each directory created above (if it contains a certain no of files)
my_dict = {f'list_{i}': [] for i in range(10)}
for i in range(10):
    if len(os.listdir(f"{new_path}/root_data_{i}")) == no_of_cores:
        for file in os.listdir(f"{new_path}/root_data_{i}"):
            my_dict[f"list_{i}"].append(file)

# this is a for loop to merge all the files within the dir
# if the directory has the required no of files
for i in range(10):
    if len(os.listdir(f"{new_path}/root_data_{i}")) == no_of_cores:
        with open(f"{new_path}/root_data_{i}/merged_file{i}.txt", "w") as new_merged_file:
            for name in my_dict[f"list_{i}"]:
                with open(f"{new_path}/root_data_{i}/{name}") as file:
                    content = file.read()
                    new_merged_file.write(content + "\n")

merged_file_to_append = [f"{new_path}/root_data_{i}/merged_file{i}.txt" for i in range(10)]
# take a closer look here, to see if after we merge file we obtain a txt file or not
merged_file_exists = all(f"merged_file{i}.txt" in os.listdir(f"{new_path}/root_data_{i}") for i in range(10))

if merged_file_exists:
    with open(f"{new_path}/final_merged_file.txt", "w") as new_merged_file:
        for m_file in merged_file_to_append:
            with open(m_file) as file:
                content = file.read()
                new_merged_file.write(content)

# alternative for files that are not .txt, using the command line
# we can change .txt to .root I suppose? I should ask

# if merged_file_exists:
#     os.system(f"cat merged_file*.txt > {new_path}/final_merged_file.txt")

# ce trebuie sa mai fac?! sa implementez partea de rulare in background
