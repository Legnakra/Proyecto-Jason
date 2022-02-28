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
            print ("No se han encontrado coincidencias.")



#Opción 3 del menú
    elif opcion == 3:
        fecha = input("Introduzca el año y se mostrará el nombre de los premiados y su categoría del premio: ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - PREMIADOS DE",fecha, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        premiados =PremiadosAno (fecha,nobel)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



#Opción 4 del menú
    elif opcion ==4:
        apellido = input("Introduzca el apellido del premiado: ")
        print("\n")
        print("- - - - - - APELLIDO: ",apellido,"- - - - -")
        print()
        premiado = EncontrarPremiado(apellido,nobel)

    

#Opción 5 del menú
    elif opcion ==5:
        print ("Las categorías son: Economics, Literature, Chemistry, Peace, Medicine, Physics.")
        categoria = input("Introduzca una categoría: ")
        year = input ("Introduzca un año: ")
        print("- - - - - - PREMIADOS:- - - - -")
        print("- - - AÑO",year,"- - - - - - - ")
        print("- - - CATEGORIA",categoria,"- - - - - - - ")
        print()
        compartido = PremioCompartido (nobel,year,existe,categoria)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



#Opción 0 del menú
    else: 
        print("La opción elegida no es válida.")
    opcion = int(input("Introduzca la opción deseada: "))
print ("Hasta pronto.")
