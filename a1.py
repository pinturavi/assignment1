import functools


def starts_withaorz(e):
    return e.startswith(("a", "A", "z", "Z"))


def change_if_starts_with_a_or_z(e, mapper):
    return mapper(e) if starts_withaorz(e) else e


def change_case(paragraph, mapper):
    return functools.reduce(lambda a, b: f"{a} {b}",
                            [change_if_starts_with_a_or_z(e, mapper) for e in paragraph.split(" ")], "")


def count_words(e):
    return len(e.split(" "))


def main():
    # input_string = input("Enter a String: > ")
    fptr = open("names.txt", "r")
    input_string = functools.reduce(lambda a, b: str(a) + str(b), fptr.readlines(), "")
    print(f"number of words : {count_words(input_string)}")
    print(f"upper case result: {change_case(input_string, lambda e: e.upper())}")
    print(f"upper case result: {change_case(input_string, lambda e: e.lower())}")


if __name__ == "__main__":
    main()