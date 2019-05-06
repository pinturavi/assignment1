from functools import reduce


def print_odd_numbers(numbers):
    [print(i, end="") if i % 2 == 1 else print("") for i in numbers]


def get_count_dict(names):
    return dict(map(lambda e: (e, len(e)), names))


def filter_even_numbers(numbers):
    return list(filter(lambda e: e % 2 == 0, numbers))


def get_sum(numbers):
    return reduce(lambda a, b: a + b, numbers)


def main():
    print_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print()
    print(get_count_dict(["elephant", "dog", "cat"]))
    print(filter_even_numbers(range(1, 100)))
    print(get_sum(range(1, 100)))


if __name__ == '__main__':
    main()
