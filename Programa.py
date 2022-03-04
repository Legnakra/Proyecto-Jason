#Importar json
import json

#Importar nobel.json
with open("nobel.json") as fichero:
    nobel = json.load(fichero)

#Importamos las funciones
from Funciones import *

#Menú del programa
print("\n")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("- - - - - - - - - - - - - - - - - - - - - - - - ~ ~ MENÚ ~ ~ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
print("1. Listar las categorías de premios nobel que se han entregado.")
print("2. Cuenta el número de premiados del año introducido por teclado.")
print("3. Buscar el año y muestra los premiados con sus categorías y nombre.")
print("4. Buscar el apellido y muestra categoría, año y motivación.")
print("5. Busca una categoría y año y muestra el ganador. Si ha compartido premio, mostrara el nombre de los mismos.")
print("0. Salir.")
print()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



#Pedir por teclado la opción deseada del menú. En caso de error, mostrar mensaje.
opcion =int(input("Introduzca la opción deseada: "))
while opcion !=0:



#Opción 1 del menú
    if opcion ==1:
        print("\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - CATEGORIAS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        categorias = ListarCategorias(nobel)
        for elemento in zip (categorias):
            print (list(map(str.strip, elemento)))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



#Opción 2 del menú
    elif opcion ==2:
        fecha = input("Introduzca el año del que desea obtener el número de premiados: ")
        mostrar_num = ContarPremiados(fecha,nobel)
        if mostrar_num >0:
            print("- - - - - - - - - - - - - - - - - - - NÚMERO PREMIADOS DE",fecha, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print()
            print("Son un total de", mostrar_num)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print ("No existen premiados de dicho año.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


#Opción 3 del menú
    elif opcion == 3:
        fecha = input("Introduzca el año y se mostrará el nombre de los premiados y su categoría del premio: ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - PREMIADOS DE",fecha, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        nombres, apellidos, categorias,existe =PremiadosAno (fecha,nobel,existe)
        if existe==0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("No existen premiados en el año introducido.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            for nombre,apellido,categoria in zip (nombres, apellidos, categorias):
                print("Nombre: ",nombre)
                print("Apellido: ",apellido)
                print("Categoria: ",categoria)
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



#Opción 4 del menú
    elif opcion ==4:
        apellido = input("Introduzca el apellido del premiado: ")
        nombres,apellidos,categorias,motivaciones,fechas,existe = EncontrarPremiado(apellido,nobel,existe)
        if existe ==0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("No existen premiados con dicho apellido.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            for nombre,apellido,categoria,motivacion,fecha in zip (nombres,apellidos,categorias,motivaciones,fechas):
                print("\n")
                print("- - - - - - APELLIDO: ",apellido,"- - - - -")
                print()
                print("Nombre: ",nombre)
                print("Apellido: ",apellido)
                print("Categoria: ",categoria)
                print("Motivación: ",motivacion)
                print("Año: ",fecha)
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    

#Opción 5 del menú
    elif opcion ==5:
        print ("Las categorías son: Economics, Literature, Chemistry, Peace, Medicine, Physics.")
        categoria = input("Introduzca una categoría: ")
        year = input ("Introduzca un año: ")
        nombres,apellidos,categorias,existe = PremioCompartido (nobel,year,categoria,existe)
        if existe ==0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("No existen premiados de ese año y categoria.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        else:    
            for nombre,apellido,categoria in zip (nombres, apellidos, categorias):
                print("- - - - - - PREMIADOS:- - - - -")
                print("- - - AÑO",year,"- - - - - - - ")
                print("- - - CATEGORIA",categoria,"- - - - - - - ")
                print()
                print("Nombre: ",nombre)
                print("Apellido: ",apellido)
                print("Categoria: ",categoria)
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



#Opción 0 del menú
    else: 
        print("La opción elegida no es válida.")
    opcion = int(input("Introduzca la opción deseada: "))
print("- - - - - - - - - - - - - - - - - - - - - - - - ")
print ("Hasta pronto.")
print("- - - - - - - - - - - - - - - - - - - - - - - - ")