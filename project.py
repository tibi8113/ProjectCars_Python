import functions as f

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear coches.
my_car = f.Car('Audi' , 'A4' , 2015 , 'Red')
my_car2 = f.Car('Ford' , 'Mustang' , 2016)
my_electric_car = f.ElectricCar('Tesla' , 'S' , 2016, 'Cian')

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear metodos.
my_car.add_fuel(50)

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear almacen.
myWareHouse1 = f.WareHouse('Volkswagen' , 'Munich')

#Añadir los coches al almacen.
myWareHouse1.add_car(my_car)
myWareHouse1.add_car(my_car2)
myWareHouse1.add_car(my_electric_car)

print(my_car)

"""-----------------------------------------------------------------------------------------------------------------------------------"""

""" Crear lista e imprimirla (Modelo cutre)
#Lista de coches
lista_coches = []
lista_coches.append(my_car)
lista_coches.append(my_car2)

#Print de todos los coches.
for car in lista_coches:
    print(car)
"""

#print("Make: " + my_car.make + "; " + "Model: " + my_car.model + "; " + "Color: " + my_car.color)
#print("Make: " + my_car2.make + "; " + "Model: " + my_car2.model + "; " + "Color: " + my_car2.color)
