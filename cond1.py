from inputs import get_int

x = get_int("Enter a number > ")

y = get_int("Enter another number > ")


if x > y:
    print(f"{x} is greater than {y}")

elif x <  y:
    print(f"{x} i less than {y}")

else:
    print(f"{x} is equal to {y}")


