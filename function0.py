from inputs import get_int


def get_max(x , y):
    return x if x > y else y


def get_min(x , y):
    return x if x < y else y


def main():
    x = get_int()
    y = get_int()
    print(get_max(x, y))


if __name__ == '__main__':
    main()