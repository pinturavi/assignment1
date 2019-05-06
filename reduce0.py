from functools import reduce


def get_sum(numbers):
    return reduce(lambda x, y: x + y, numbers, 0)


# def get_sum(numbers):
#     result = 0
#
#     for e in numbers:
#         result += e
#
#     return result


print(get_sum([2, 4, 6, 7, 8]))

