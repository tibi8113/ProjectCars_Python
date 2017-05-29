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
    opc2 = input("¿En que marca de coche estás interesado?\n").title()
    print ("-------------------------------------------------------------------------------------")

#Coger marca introducida e imprimir los coches de esa misma marca.
    lista_coches = all_cars.find_car(opc2)
    for c in lista_coches:
        print(c)

    opc3 = input("¿Que modelo deseas?\n")
    print ("-------------------------------------------------------------------------------------")
    listar_modelo = all_cars.find_car_model(opc3)
    for m in listar_modelo:
        print(m)

        


"""-----------------------------------------------------------------------------------------------------------------------------------"""

"""
    if opc2 == "AUDI":
        for c in all_cars.cars:
            if c.make == "Audi":
                print(c)

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

