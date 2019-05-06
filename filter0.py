
def gt_3(numbers):
    return list(filter(lambda e: e > 3, numbers))

# def gt_3(numbers):
#     result = []
#     for i in numbers:
#         if i > 3:
#             result.append(i)
#     return result


print(gt_3([1, 2, 3, 4, 5]))
