#RETO 10 - Parte 1
#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

def introducir():
    #Se crea el arreglo
    cantidad_numeros : int = int(input("Introduzca el número de elementos que tiene el arreglo: "))
    numeros : list = []
    #Se ingresan los elementos del arreglo
    for i in range(cantidad_numeros):
        numeros += [float(input("Ingrese el número: "))]
    #Se obtiene el promedio de los números
    promedio(numeros,cantidad_numeros)
    return

def promedio(numeros : list,cantidad_numeros : list):
    prom : float = 0
    #Se suman todos los elementos del arreglo
    for j in range(cantidad_numeros):
        prom += numeros[j]
    #Se divide la suma en el total de elementos
    promedio_total : float = prom/cantidad_numeros
    print(f"El promedio de los números {numeros} es igual a {promedio_total}")
    return

def continuar():
    #El usuario decide si quiere volver a correr el programa
    opcion : int = int(input("¿Desea continuar? Marque 1 (Sí) o 2 (No): "))
    return opcion

if __name__ == "__main__":
    #Inicia el programa
    print("Programa para conocer el promedio de in arreglo de reales.")
    #Se crea un ciclo para poder repetir el programa tantas veces como desee el usuario
    while True:
        introducir()
        opcion : int = continuar()
        #El usuario decide si desea continuar
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("SintaxError")
            break

# ! /\|=\/