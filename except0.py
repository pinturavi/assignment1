
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("exception occured.")
        return 0


print(divide(4, 0))