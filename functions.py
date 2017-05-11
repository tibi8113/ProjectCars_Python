class Car():

    def __init__(self, make, model, year, color='White'):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_capacity = 100
        self.fuel_level = 0

    def __str__(self):
        return "Car - Make: %s, Model: %s, Color: %s, Fuel: %s" % (self.make, self.model, self.color, self.fuel_level)

    #Repostar
    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel to "+ self.make + ".")
        else:
            print("The tank won't hold that much.")

class ElectricCar(Car):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
        #Tamaño de la bateria.
        self.battery_size = 100
        #Nivel de bateria en %.
        self.charge_level = 0

class WareHouse():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars = []

    
    def add_car(self, car):
        #Añadir un coche al WareHouse.
        self.cars.append(car)

    
    def remove_car(self, car):
        #Quitar un coche del WareHouse.
        self.cars.append(car)