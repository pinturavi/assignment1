from inputs import get_int

SIZE = 3


def chart(scores, n):
    for i in range(n):
        for j in range(scores[i]):
            print("#", end="")
        print()


def main():
    scores = []
    for i in range(SIZE):
        scores.append(get_int())

    chart(scores, SIZE)


if __name__ == '__main__':
    main()
