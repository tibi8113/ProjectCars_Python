import functions as f
import data as d

def menu2():
    opc2 = input("¿En que marca de coche estás interesado?\n").title()
    print ("-------------------------------------------------------------------------------------")

    #Coger marca introducida e imprimir los coches de esa misma marca.
    lista_coches = all_cars.find_car(opc2)
    for c in lista_coches:
        print(c)

    opc3 = input("¿Que modelo deseas?\n")
    print ("-------------------------------------------------------------------------------------")
    coche_seleccionado = all_cars.find_car_model(opc3)

    print(coche_seleccionado)
        
    opc4 = input("1.Lo quiero de serie\n2.Me gustaría personalizarlo\n")

    if opc4 == "1":
        print("El precio es " + str(coche_seleccionado.price),"euros.")
    elif opc4 == "2":

        print("¿Que deseas añadirle?")

        precio = coche_seleccionado.price
        personalizar1 = input("1.Camara 3D.\n")
        personalizar2 = input("2.Neumáticos deportivos.\n")
        personalizar3 = input("3.Equipo de música avanzado.\n")

        print(str(precio))
        if personalizar1 == "si":
            precio = precio + 350
            print(str(precio))
        if personalizar2 == "si":
            precio = precio + 225
            print(str(precio))
        if personalizar3 == "si":
            precio = precio + 500
            print(str(precio))

 
        print("El precio es " + str(precio) + " euros.")

        


def menu1():
    #Imprimir todos los coches del WareHouse1
    print (myWareHouse1.name)
    for coche in myWareHouse1.cars:
        print(coche)

    print ("-------------------------------------------------------------------------------------")

    #Imprimir todos los coches del WareHouse2
    print (myWareHouse2.name)
    for coche in myWareHouse2.cars:
        print(coche)
    menu2    




"""-----------------------------------------------------------------------------------------------------------------------------------"""

#Crear almacen.
myWareHouse1 = f.WareHouse('WareHouse1', 'Munich')
myWareHouse2 = f.WareHouse('WareHouse2', 'Munich')



#Meter los coches en los almacenes correspondientes
all_cars = f.Cars(d)
for c in all_cars.cars:
    if c.type == "Electric":
        myWareHouse2.add_car(c)
    else:
        myWareHouse1.add_car(c) 

"""-----------------------------------------------------------------------------------------------------------------------------------"""
#Opciones
opc = input("1.Ver catálogo\n2.Comprar coche\n")

if opc == "1":
    menu1()


    menu2()














"""-----------------------------------------------------------------------------------------------------------------------------------"""

"""
print("El precio es " + str(coche_seleccionado.price) + "+ 15% = " + str(coche_seleccionado.price * 1.15))

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

