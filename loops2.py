from inputs import get_int


def get_positive_int():
    while True:
        result = get_int()
        if result > 0:
            break

    return result


print(get_positive_int())

