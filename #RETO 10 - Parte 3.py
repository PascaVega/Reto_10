#RETO 10 - Parte 3
#Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

def introducir():
    #Se crea el arreglo con solo números naturales
    num_elementos : int = int(input("Ingrese el número de elementos del arreglo: "))
    arreglo : list = []
    #Se añaden los elmentos al arreglo
    for i in range(num_elementos):
        arreglo.append(int(input(f"Ingrese el elemento {i+1} del arreglo (siendo el número un natural): ")))
    #Se separan los ceros
    separar_ceros(num_elementos,arreglo)
    return

def separar_ceros(num_elementos : int, arreglo : list):
    #Se crea un nuevo arreglo
    nuevo_arreglo : list = []
    for j in range(num_elementos):
        #Se separan los dijistos de cada elemento
        cadena_numero = str(arreglo[j])
        digitos : list = [int(digito) for digito in cadena_numero]
        #Se cuenta el número de ceros que hay en la cadena
        num_ceros : int =+ digitos.count(0)
        #Se eliminan los ceros de la cadena
        for k in range(num_ceros):
            digitos.remove(0)
        numero = 0
        #Se insertan los elementos (ya sin ceros) al nuevo arreglo
        for digito in digitos:
            numero = numero * 10 + digito
        nuevo_arreglo.insert(j,numero)
        #Se añaden los ceros de la cadena al final
        for l in range(num_ceros):
            nuevo_arreglo.append(0)
    #Se imprime el resultado
    print(f"El arreglo es {nuevo_arreglo}")
    return

def continuar():
    #El usuario decide si desea repetir el programa
    opcion : int = int(input("¿Desea continuar? Marque 1 (Sí) o 2 (No): "))
    return opcion

if __name__ == "__main__":
    print("Programa para dejar al final todos los ceros que aparezcan en un arreglo.")
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