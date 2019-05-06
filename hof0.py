from functools import reduce
# def get_sum(numbers):
#     result = 0
#     for e in numbers:
#         result += e
#     return result
#
#
# def get_sum_odd(numbers):
#     result = 0
#     for e in numbers:
#         if e %2 == 1:
#             result += e
#     return result
#
#
# def get_sum_even(numbers):
#     result = 0
#     for e in numbers:
#         if e %2 == 0:
#             result += e
#     return result


def get_sum(numbers,predicate=lambda e: True,):
    return reduce(lambda x, y: x+y, filter(predicate, numbers), 0)


def main():
    print(get_sum([1, 2, 3, 4, 5]))
    print(get_sum([1, 2, 3, 4, 5], lambda e: e % 2 == 0))
    print(get_sum([1, 2, 3, 4, 5], lambda e: e % 2 == 1))
    print(get_sum([1, 2, 3, 4, 5], lambda e: e % 2 == 1 and e > 5))
    # print(get_sum_odd([1, 2, 3, 4, 5]))
    # print(get_sum_even([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()