# q7.py - Classes/Objects
# Author: ph wong
# Date: March 2026

class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    
    def __init__(self, make, model, year):
        """Initialize car with make, model, year"""
        self.make = make
        self.model = model
        self.year = year
    
    def describe_car(self):
        """Print car info as Year Make Model"""
        print(f"{self.year} {self.make} {self.model}")


# Task 2
# Create Toyota Corolla 2020 and describe it
my_car = Car("Toyota", "Corolla", 2020)
my_car.describe_car()