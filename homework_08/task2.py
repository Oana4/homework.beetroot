def operation():
    try:
        a = input('Choose first number: ')
        b = input('Choose second number: ')
        print(int(a) ** 2 / int(b))
    except ValueError:
        print("Your a and be cannot be converted to integers")
    except ZeroDivisionError:
        print("We can't divide by 0!")


operation()






