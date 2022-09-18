i = 1
huge_list = []
math_list = []

while i <= 100:
    huge_list.append(i)
    if i % 7 == 0 and i % 5 != 0:
        math_list.append(i)
    i += 1

print(huge_list)
print(math_list)



