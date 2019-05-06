class Dog:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_legs():
        return 4


def main():
    buddy = Dog("buddy")
    print(buddy.name)
    print(Dog.get_legs())


if __name__ == '__main__':
    main()
