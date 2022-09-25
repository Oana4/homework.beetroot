# Write a Python program to find the list in a list of lists whose sum_of_items of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]

list_of_sample_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

biggest_sum = 0
biggest_list = []

for each_list in list_of_sample_lists:
    sum_of_items = 0
    for item in each_list:
        sum_of_items += item
    if sum_of_items > biggest_sum:
        biggest_sum = sum_of_items
        biggest_list = each_list

print(biggest_list)

