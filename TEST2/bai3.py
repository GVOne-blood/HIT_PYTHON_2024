class Vehicle:
    def __init__(self, make):
        self.make = make
    def description(self):
        print(self.make)
class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model
    def description(self):
        super().description()
        print(self.model)
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    def description(self):
        super().description()
        print(self.battery_size)
Ve = Vehicle("Honda")
Ve.description()
car = Car("Honda", "nu")
car.description()
ecar = ElectricCar("Honda", "nu", 200)
ecar.description()