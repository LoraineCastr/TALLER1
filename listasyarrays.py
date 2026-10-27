#Taller1
#Comparacion entre listas y arrays

import numpy as np 
import time 

#cantidad de datos que se van a procesar 
datos = 500000

#dos listas con los misma cantidad de datos
lista = list(range(datos))
array = np.arange(len(lista))

#Medir el tiempo de recorrido de la lista
inicio = time.perf_counter()
valor_lista = [n * 2 for n in lista]
tiempo_lista = time.perf_counter() - inicio
