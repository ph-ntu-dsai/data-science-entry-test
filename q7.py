class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(self.year, self.make, self.model)


x = Car("Toyota", "Corolla", 2020)
x.describe_car()
