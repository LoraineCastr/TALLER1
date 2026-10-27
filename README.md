#Taller de Listas y Arrays

INFORME DE ANALISIS Y CONCLUSIONES DE RENDIMIENTO

--Descripcion
Para realizar la comparación se creó una cantidad de 80 millónes de datos enteros. Después, se multiplicó cada número por dos, utilizando inicialmente una lista de Python y luego utilizando un array de NumPy.

La creación de las estructuras se realizó antes de iniciar el cronómetro, de manera que la medición se concentrara en el procesamiento de los datos. 

Se utilizó la función time.perf_counter() para medir el tiempo que tarda cada operación. 
Finalmente, se compararon los resultados para verificar que ambas estructuras produjeran los mismos valores y identificar que metodo
realiza la ejecucion mucho mas rapido.

--Resultados Obtenidos en la medicion del Rendimiento
Se registraron los siguientes resultados, despues de ejecutar el programa

Puntos Evaluados   | Lista (Python)  | Array (Numpy)
Cantidad de datos  | 80.000.000      |  80.000.000
Operacion realizada| Multiplicado x2 | Multiplicado x2
Tiempo de ejecucion| 22.508048 seg   |  6.046422 seg
igual cantidad de  |    TRUE         |     TRUE
datos              |

--Analisis comparativo entre las listas y arrays
En los ejercicios de pruebas realizados, arrays duro menos tiempo en ejecutar la misma cantidad de datos, eso permite determinar que la forma en como procesa los datos es mucho mas rapido y eficiente en el rendimiento del programa, puede variar los recursos disponible durante la ejecucion.



--Respuestas del reto

¿Qué diferencias observas en el tiempo de ejecución al realizar la misma operación con una lista y con un array, y a qué crees que se deben esas diferencias?

La lista y el array no tardan lo mismo en completar la ejecucion, siempre varia su resultado, 
Array -Numpy es mas rapido para trabajar con grandes cantidades de datos numericos, lo cual permite realizar operaciones sobre todo el array sin tener que ejecutar un ciclo para cada elemento.
La lista demora un mucho mas su procesamiento ya que debe comprender la operacion a realizar y hace el proceso de cada elemento de forma individual.

el array, tiene una mejor forma de procesar muchos calculos numericos.
¿Cómo influye la forma en que cada estructura almacena los datos en memoria
en el rendimiento obtenido durante la ejecución?
Las listas almacenan referencias a objetos, por lo que cada dato puede tener su propia representación en memoria. Esto ofrece flexibilidad, ya que una misma lista puede contener diferentes tipos de datos.
Los arrays, cuando tienen un tipo dato definido, almacenan sus elementos en una representación más uniforme y contigua en memoria. Esto permite aprovechar mejor la memoria y ejecutar operaciones numéricas mediante rutinas optimizadas.


Si tuvieras que elegir una de estas estructuras para procesar grandes
volúmenes de datos numéricos, ¿cuál seleccionarías y por qué? 

Para realizar procesos con grande cantidades de datos numéricos, elegiría los arrays de NumPy, si se deben realizar operaciones matemáticas de manera repetida.
La razón es que permiten aplicar operaciones sobre muchos elementos utilizando operaciones logicas, como multiplicar un array completo por dos. Además, suelen aprovechar implementaciones optimizadas para realizar cálculos numéricos.
 