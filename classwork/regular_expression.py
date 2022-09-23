import re

pattern = re.compile(r'\+\d{3}\s\d{3}\s\d{3}\s\d{3}')
test_string = '+420 777 803 999'
result = re.match(pattern, test_string)

if result:
    print("Good number!")
else:
    print("Wrong number format!")
