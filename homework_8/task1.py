def oops():
    raise IndexError("It seems to be an index error!")


try:
    oops()
except IndexError:
    print("We detected an index error!")
