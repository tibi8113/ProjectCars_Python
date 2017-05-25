class Car():

    def __init__(self, make, model, year, color, price, tipo):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.type = tipo
        self.fuel_capacity = 100
        self.fuel_level = 0

    def __str__(self):
        return "Car - Make: %s, Model: %s, Color: %s, Price: %s euros, Type: %s" % (self.make, self.model, self.color, self.price, self.tipo)


    #Repostar
    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel to "+ self.make + ".")
        else:
            print("The tank won't hold that much.")

class ElectricCar(Car):
    def __init__(self, make, model, year, color, price, tipo):
        super().__init__(make, model, year, color, price, tipo)
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

    
'''
#Método alternativo para imprimir coches    
    def __str__(self):
        s = ""
        for c in self.cars:
            s += c.make + " " + c.model + " " + c.color + "/n"
        return s

#Métono alternativo para imprimir coches con un print
    def print_all_cars(self):
        for coche in self.cars:
            print(coche.make)

'''


