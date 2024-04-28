#RETO 10 - Parte 2
#Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

def introducir():
    #Se crea el primer arreglo
    num_elementos : int = int(input("Ingrese el número de elementos de los arreglos: "))
    elementos_1 : list = []
    print("Arreglo 1:")
    #Se crean los elementos del arreglo
    for i in range(num_elementos):
        elementos_1 += [float(input(f"Ingrese el elemento {i+1} del primer arreglo: "))]
    #Se crea el segundo arreglo
    elementos_2 : list = []
    print("Arreglo 2:")
    #Se crean los elementos del arreglo
    for j in range(num_elementos):
        elementos_2 += [float(input(f"Ingrese el elemento {j+1} del segundo arreglo: "))]
    #Se obtiene el producto punto
    producto_punto(elementos_1,elementos_2,num_elementos)
    return

def producto_punto(elementos_1 : list,elementos_2 : list,num_elementos : int):
    #Se crea otra lista para ir almacenando las multiplicaciones
    multiplicaciones : list = []
    for k in range(num_elementos):
        multiplicaciones += [elementos_1[k]*elementos_2[k]]
    #Nueva variable para almacenar la suma de las mmultipicaciones
    suma_final : float = 0
    for l in range(num_elementos):
        suma_final += multiplicaciones[l]
    #Se imprime el resultado
    print(f"El producto punto de los arreglos es: {suma_final}")
    return

def continuar():
    #El usuario decide si quiere volver a correr el programa
    opcion : int = int(input("¿Desea continuar? Marque 1 (Sí) o 2 (No): "))
    return opcion

if __name__ == "__main__":
    print("Programa para conocer el producto punto de dos arreglos con la misma contidad de elementos.")
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