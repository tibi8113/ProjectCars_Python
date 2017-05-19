import functions as f

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear coches.
my_car1 = f.Car('Audi' , 'A7' , 2017 , 'Red')
my_car2 = f.Car('Ford' , 'Mustang' , 2017, 'White')
my_electric_car1 = f.ElectricCar('Tesla' , 'S' , 2017, 'Deep Blue')
my_electric_car2 = f.ElectricCar('Passat', 'GTE', 2017, 'Grey')

"""-----------------------------------------------------------------------------------------------------------------------------------"""

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear almacen.
myWareHouse1 = f.WareHouse('MTC', 'Munich')

#Añadir los coches al almacen.
myWareHouse1.add_car(my_car1)
myWareHouse1.add_car(my_car2)
myWareHouse1.add_car(my_electric_car1)
myWareHouse1.add_car(my_electric_car2)

"""-----------------------------------------------------------------------------------------------------------------------------------"""

print('¿En qué coche estás interesado?')
#Imprimir Todos los coches (solo marca)
print('Estos son los coches disponibles: ' + f.cars[car1])


"""-----------------------------------------------------------------------------------------------------------------------------------"""

'''
#Añadir combustible.
my_car1.add_fuel(50)
'''

for coche in myWareHouse1.cars
    print(coche.make)