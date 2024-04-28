# Reto 10
| Nombre                 | Identificación | Grupo | Trabajo          |
|------------------------|----------------|-------|------------------|
| Angélica Pascagaza Vega| 1031652163     |   5   | Trabajo individual |

## Solución del reto
<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 10 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se creo un arreglo de <i>n</i> elementos, el usuario inserta los elementos del arreglo yluego se obtiene el promedio.</td>
  </tr>
</table>

**Parte 1**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 10 - Parte 2</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Ambos arreglos constan de <i>n</i> elementos, el usuario ingresa los elementos y depués se calcula el producto punto.</td>
  </tr>
</table>

**Parte 2**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 10 - Parte 3</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, se parte de un arreglo de <i>n</i> elementos, los cuales cada uno se convierte en una cadena de texto, luego se paran los ceros de cada elemento y final mente se crea un nuevo arreglo para insertar todos los elementos ya modificados más los ceros al final de este.</td>
  </tr>
</table>

**Parte 3**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 9 - Parte 4</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Algoritmos de ordenación</b>
      <li>Son un <b>conjunto de instrucciones</b> que toman un arreglo o lista como entrada y organizan los elementos en un <b>orden particular</b>.</li>
    </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Bubble sort --> burbuja</b>: es uno de los algoritmos de sorting más simples y básicos. Funciona comparando repetidamente los elementos consecutivos de la lista y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que no se requieren más intercambios, lo que significa que la lista está ordenada.</td>
    <tr bgcolor="#e4e4ed">
      <td style="color:#141414">En cortas palabras, Bubble sort funciona de la siguiente manera:
      <ol>
        <li>Comienza desde el primer elemento de la lista y compara cada par de elementos adyacentes.</li>
        <li>Si el primer elemento de un par es mayor que el segundo, los intercambia.</li>
        <li>Luego, pasa al siguiente par de elementos adyacentes y repite el proceso.</li>
        <li>Continúa este proceso hasta llegar al final de la lista.</li>
        <li>Una vez que se completa una pasada completa por la lista, el elemento más grande estará en la última posición.</li>
        <li>Repite el proceso para los elementos restantes de la lista, excluyendo el último elemento que ya está en su posición correcta después de la primera pasada.</li>
        <li>Continúa este proceso hasta que no se realicen más intercambios en una pasada completa por la lista, lo que indica que la lista está ordenada.</li>
      </ol>
      </td>
    </tr>
    

  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center"><b>Algunos algoritmos de ordenación comunes son:</b> 
      <li>Selection sort --> selección</li>
      <li>Insertion sort --> inserción</li>
      <li>Merge sort --> combinación</li>
      <li>Quick sort --> rápida</li>
      <li>Heap sort --> montón</li>
      <li>Counting sort --> conteo</li>
      <li>Radix sort --> raíz</li>
      <li>Bucket sort --> cubo</li>
    </td>
  </tr>
</table>

<h2>Bibliografía</h2>
    <div class="bibliografia">
        <table>
            <tr>
                <th>Referencias</th>
            </tr>
            <tr>
                <td>GeeksforGeeks. (s. f.). Bubble Sort Algorithm. Recuperado de https://www.geeksforgeeks.org/bubble-sort/<a href="https://www.geeksforgeeks.org/bubble-sort/"></a></td>
            </tr>
            <tr>
                <td>DelftStack. (s. f.). Bubble Sort Algorithm in Python. Recuperado de https://www.delftstack.com/es/tutorial/algorithm/bubble-sort/#google_vignette<a href="https://www.delftstack.com/es/tutorial/algorithm/bubble-sort/#google_vignette"></a></td>
            </tr>
            <tr>
                <td>freeCodeCamp. (s. f.). Algoritmos de ordenación explicados con ejemplos en JavaScript, Python, Java y C. Recuperado de https://www.freecodecamp.org/espanol/news/algoritmos-de-ordenacion-explicados-con-ejemplos-en-javascript-python-java-y-c<a href="https://www.freecodecamp.org/espanol/news/algoritmos-de-ordenacion-explicados-con-ejemplos-en-javascript-python-java-y-c"></a></td>
            </tr>
        </table>
    </div>
