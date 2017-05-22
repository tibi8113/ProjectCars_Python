import functions as f

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear coches.
my_car1 = f.Car('Audi', 'A7', 2017, 'Red', 65000)
my_car2 = f.Car('Ford', 'Mustang', 2017, 'White', 45000)
my_electric_car1 = f.ElectricCar('Tesla', 'S' , 2017, 'Deep Blue', 85000)
my_electric_car2 = f.ElectricCar('Passat', 'GTE', 2017, 'Grey', 48000)

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
opc = input("1.Ver catálogo\n2.Comprar coche\n")

print('¿En qué coche estás interesado?')
#Imprimir Todos los coches (solo marca)
for coche in myWareHouse1.cars:
    print(coche.make)

opc = input().upper()
if opc == "AUDI":
    print(my_car1)
elif opc == "FORD":
    print(my_car2)
elif opc == "TESLA":
    print(my_electric_car1)
elif opc == "PASSAT":
    print(my_electric_car2)
"""-----------------------------------------------------------------------------------------------------------------------------------"""

'''
#Añadir combustible.
my_car1.add_fuel(50)
'''

