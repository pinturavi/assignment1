from inputs import get_int


def chart(score_list):
    for i in range(len(score_list)):
        for j in range(score_list[i]):
            print("#", end="")
        print()


if __name__ == '__main__':
    scores = []
    for index in range(3):
        scores.append(get_int())

    chart(scores)
