class Vehicle:

    def __init__(self, wheels, doors=4):
        self.wheels = wheels
        self.doors = doors

    def crankEngine(self):
        print("Vroom")


class Car(Vehicle):

    def __init__(self, wheels, make, model, doors=4):
        super().__init__(wheels, doors)
        self.make = make
        self.model = model


class AutoPilot:

    def calculateRoute(self, destination="there"):
        start = "here"
        wayPoints = [start, destination]
        return wayPoints


class ElectricCar(Car, AutoPilot):

    def __init__(self, wheels, make, model, doors=4):
        super().__init__(wheels, make, model, doors)

    def crankEngine(self):
        print("...")




tesla = ElectricCar(4,"Telsa","Model C")
tesla.crankEngine()
print("Calculate Route:", tesla.calculateRoute())
print("Electric Car MRO:", ElectricCar.__mro__)
print("Car MRO:", Car.__mro__)