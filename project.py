import functions as f
import data as d

"""-----------------------------------------------------------------------------------------------------------------------------------"""
"""
#Crear coches.
my_car1 = f.Car('Audi', 'A7', 2017, 'Red', 66000)
my_car2 = f.Car('Audi', 'Q7', 2017, 'Grey', 65000)
my_car3 = f.Car('Ford', 'Mustang', 2017, 'White', 45000)
my_car4 = f.Car('Ford', 'Focus RS', 2017, 'Blue', 40000)
my_electric_car1 = f.ElectricCar('Tesla', 'S' , 2017, 'Deep Blue', 85000)
my_electric_car2 = f.ElectricCar('Tesla', 'X', 2017, 'White', 97000)
my_electric_car3 = f.ElectricCar('Volkswagen', 'Passat GTE', 2017, 'Grey', 48000)
my_electric_car4 = f.ElectricCar('Volkswagen', 'Golf GTE', 2017, 'Dark Iron', 40000)
"""

"""-----------------------------------------------------------------------------------------------------------------------------------"""

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear almacen.
myWareHouse1 = f.WareHouse('MTC', 'Munich')
"""
#Añadir los coches al almacen.
myWareHouse1.add_car(my_car1)
myWareHouse1.add_car(my_car2)
myWareHouse1.add_car(my_car3)
myWareHouse1.add_car(my_car4)
myWareHouse1.add_car(my_electric_car1)
myWareHouse1.add_car(my_electric_car2)
myWareHouse1.add_car(my_electric_car2)
myWareHouse1.add_car(my_electric_car2)
"""

"""-----------------------------------------------------------------------------------------------------------------------------------"""
opc = input("1.Ver catálogo\n2.Comprar coche\n")

print('¿En qué coche estás interesado?')
#Imprimir Todos los coches (solo marca)
for coche in myWareHouse1.cars:
    print(coche.make)

opc = input().upper()
if opc == "AUDI":
    print(my_car1)
    print(my_car2)
elif opc == "FORD":
    print(my_car3)
    print(my_car4)
elif opc == "TESLA":
    print(my_electric_car1)
    print(my_electric_car2)
elif opc == "PASSAT":
    print(my_electric_car3)
    print(my_electric_car4)
"""-----------------------------------------------------------------------------------------------------------------------------------"""

'''
#Añadir combustible.
my_car1.add_fuel(50)
'''

