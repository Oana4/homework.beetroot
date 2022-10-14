from even_func import check_if_even

my_list = [1, 3, 5, 6, 9, 12, 14]
my_sum = 0

for num in my_list:
    if check_if_even(num):
        my_sum += num

print(my_sum)
