from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, model, color):
        self.model = model
        self.color = color

    @abstractmethod
    def no_of_wheels(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Bike(Vehicle):

    def __init__(self, model, color, that_price):
        self.price = that_price
        super().__init__(model, color)

    def get_price(self):
        return self.price

    def no_of_wheels(self):
        return 2


class Car(Vehicle):

    def __init__(self, model, color, that_price):
        self.price = that_price
        super().__init__(model, color)

    def get_price(self):
        return self.price

    def no_of_wheels(self):
        return 4


if __name__ == '__main__':
    swift = Bike("xyz", "red", 5000000)
    innova = Car("abc", "black", 7000000)
    print(swift.get_price())
    print(innova.get_price())
