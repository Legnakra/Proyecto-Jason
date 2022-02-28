#Funciones de lectura para el archivo nobel.json

#Función Ejercicio 1: Listar las categorías de premios nobel que se han entregado.
def ListarCategorias(nobel):
    listado=[]
    for categoria in nobel:
        listado.append(categoria["category"])
    return (set(listado))


#Función Ejercicio 2: Cuenta el número de premiados del año introducido por teclado.
def ContarPremiados(fecha,nobel):
    id_premiados=[]
    for premiado in nobel:
        if premiado["year"]==fecha:
            for elemento in premiado["laureates"]:
                id_premiados.append(elemento["id"])
    return (len(id_premiados))


#Función Ejercicio 3: Buscar el año y muestra los premiados con sus categorías y nombre.
def PremiadosAno (fecha,nobel):
    for premiado in nobel:
        if premiado["year"]==fecha:
            for laureated in premiado["laureates"]:
                print("Nombre: ", laureated.get('firstname'))
                print("Apellido: ", laureated.get('surname'))
                print("Categoria: ", premiado["category"])
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
                

#Función Ejercicio 4: Buscar el apellido y muestra categoría, año y motivación.
def EncontrarPremiado(apellido,nobel):
    try:
        for elemento in nobel:
            for laureated in elemento["laureates"]:
                if laureated.get('surname') == apellido:
                    print("Nombre: ", laureated.get('firstname'))
                    print("Apellido: ", laureated.get('surname'))
                    print("Motivacion: ", laureated.get('motivation'))
                    print("Categoria: ", elemento["category"])
                    print("Año:", elemento["year"])
                    print("- - - - - - - - - - - - - - - - - - - - - - - - ")
    except:
        laureated.get('surname') != apellido


#Función Ejercicio 5: Busca una categoría y año y muestra el ganador. Si ha compartido premio, mostrara el nombre de los mismos.
def PremioCompartido (nobel,year,existe,categoria):
    existe =0
    for premiado in nobel:
        if premiado["year"]==year and premiado["category"]==categoria:
            for laureated in premiado["laureates"]:
                print("Nombre: ", laureated.get('firstname'))
                print("Apellido: ", laureated.get('surname'))
                print("Categoria: ", premiado["category"])
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
                existe = 1
    if existe == 0:
        print ("No se han encontrado coincidencias.")