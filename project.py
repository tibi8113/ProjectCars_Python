import functions as f
import data as d

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear almacen.
myWareHouse1 = f.WareHouse('MTC', 'Munich')
myWareHouse2 = f.WareHouse('MTC.E', 'Munich')

"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Meter los coches en los almacenes correspondientes
all_cars = f.Cars(d)
for c in all_cars.cars:
    if c.type == "Electric":
        myWareHouse2.add_car(c)
    else:
        myWareHouse1.add_car(c)

#Opciones
opc = input("1.Ver catálogo\n2.Comprar coche\n")

if opc == "1":
    print (myWareHouse1.name)
    for coche in myWareHouse1.cars:
        print(coche)

    print ("-------------------------------------------------------------------------------------")

    print (myWareHouse2.name)
    for coche in myWareHouse2.cars:
        print(coche)

elif opc == "2":
    opc2 = input("¿En que coche estás interesado?\n")
    print ("-------------------------------------------------------------------------------------")

    print(f.Cars.find_car)
    if opc == "AUDI":
        for c in all_cars.cars:
            if c.make == "AUDI":
                print()
    elif opc == "FORD":
        pass
    elif opc == "TESLA":
        pass
    elif opc == "PASSAT":
        pass


        


"""-----------------------------------------------------------------------------------------------------------------------------------"""

"""
#Añadir combustible.
my_car1.add_fuel(50)


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
"""

