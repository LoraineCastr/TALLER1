#Taller1
#Comparacion entre listas y arrays

import numpy as np 
import time 

#cantidad de datos que se van a procesar 
datos = 10000000

#dos listas con los misma cantidad de datos
lista = list(range(datos))
array = np.arange(len(lista))

#Medir el tiempo de recorrido de la lista
inicio = time.perf_counter()
valor_lista = [n * 2 for n in lista]
tiempo_lista = time.perf_counter() - inicio

#Medir el tiempo de rocorrido del array
inicio = time.perf_counter()
valor_array = array * 2
tiempo_array = time.perf_counter() - inicio

#Cantidad de datos recorridos son iguales 
valor_iguales = np.array_equal(valor_lista, valor_array)

#Resultado del tiempo de recorrido de la lista y del array, y si la cantidad de datos es la misma 
print("Tiempo en recorrer la lista:", f"{tiempo_lista:.6f}")
print("Tiempo en recorrer el array:", f"{tiempo_array:.6f}")
print("Los datos recorridos son iguales:", valor_iguales)

