actual_name = 'oana'
match = False

while not match:
    fake_name = input('Please enter your first name: ')
    if actual_name == fake_name.lower():
        print("Hurray! There's a match")
        match = True
    else:
        print("There may be a typo. Type again your name!")

