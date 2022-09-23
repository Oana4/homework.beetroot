# Write a program which will use regex to recognize is inputted by user number - have a correct format. References:
# +420 777 803 999, +1 203 532 345 
# If number is correct - print ("Good Number!"). If not - print "Wrong number format!"

import re

pattern = re.compile(r'\+\d{3}\s\d{3}\s\d{3}\s\d{3}')
test_string = '+420 777 803 999'
result = re.match(pattern, test_string)

if result:
    print("Good number!")
else:
    print("Wrong number format!")
