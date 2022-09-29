# Create a function which will open a file by first argument (file_name), and will return first post-code in a file,
# which will contain the second argument (part_of_postcode_str)
# Advanced task: now, make it possible to put into a second argument a single value ("36235"),
# or a list of values (["36", "26"]). In a second case - function must return all post-codes
# that will suite at list one of the searching values

import json


def get_postcode(file_name, part_of_postcode_str):
    with open(file_name) as my_file:
        postcodes = json.load(my_file)
        if isinstance(part_of_postcode_str, str):
            return [zip_code for zip_code in postcodes if part_of_postcode_str in zip_code]
        elif isinstance(part_of_postcode_str, list):
            # print(set(postcodes))
            # print(set(part_of_postcode_str))
            return set(postcodes).intersection(set(part_of_postcode_str))
            # print([part_of_postcode in '33901' for part_of_postcode in part_of_postcode_str])
            # return [zip_code for zip_code in postcodes if any(part_of_postcode in zip_code for part_of_postcode
            #                                                   in part_of_postcode_str)]


print(get_postcode("zip_codes.json", ['39133']))
