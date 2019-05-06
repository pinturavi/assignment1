import functools


def get_words():
    try:
        fileptr = open("names.txt", "r")
        return functools.reduce(lambda a, b: a + b, map(lambda e: str(e).replace("\n", " "), fileptr.readlines()), "")
    finally:
        fileptr.close()


print(get_words())



