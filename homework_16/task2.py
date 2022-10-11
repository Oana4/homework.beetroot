def in_range(start: int = 0, stop: int = None, step: int = 1):
    number = start
    if start < stop and step < 0:
        print("You can't achieve stop with a negative step!")
    elif start > stop and step > 0:
        print("You can't achieve stop with a positive step!")
    else:
        while True:
            if (stop < number and step > 0) or (number < stop and step < 0):
                break
            yield number
            number += step


for item in in_range(1, 10, 2):
    print(item)