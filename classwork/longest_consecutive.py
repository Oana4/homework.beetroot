# # Write a function that takes on an input random ints (between 1 and 10) and
# # returns the longest consecutive run and the length of that run of elements of the list.
#
# Ex.     def task1.py(1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5) -> 6, 4
#     def task1.py(1) -> 1, 1
#     def task1.py() -> 0, None
#
# Then create another function which takes on input result of function from the previous step and
# prints Informative message about the longest consecutive run, something like - “Longest run is 6 of integers - 4”

def counter(*args):
    biggest_count = 1
    count = 1
    current_elem = ''
    for element in args:
        if current_elem == element:
            count += 1
            if count > biggest_count:
                biggest_count = count
                cons_element = element
        else:
            count = 1
        current_elem = element

    print(f"Number of occurrences: {biggest_count}. Tne number that occurred the most: {cons_element}")


counter(1, 3, 3, 3, 5, 5, 5, 3, 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 3, 4, 4, 4, 4, 4, 4, 4)




