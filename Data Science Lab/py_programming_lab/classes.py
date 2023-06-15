class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        return f"{self.year} {self.make} {self.model}"
    
my_car = Car('Toyota', 'Corolla', 2005)
print(my_car.display())