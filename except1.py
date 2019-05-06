
def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("second parameter should not be zero")
    except TypeError:
        print("both the inputs should be numbers")


divide("a", 2)