# MCOC-Proyecto-0
## Introducción
En este proyecto se busca mostrar el efecto de la pérdida de significancia en operaciones aritméticas, particularmente con la propiedad de la función inversa del Logaritmo Natural.
La pérdida de significancia ocurre cuando se trabaja con números que contienen ciertos errores, como pasa con los números decimales para los distintos bits que se pueden procesar. Es por esto que para este problema se verificará el resultado de la propiedad comparando con la cantidad de datos analizados con 3 listas de números idénticos, variando simplemente en el tipo de datos que sería np.float16, np.float32 y np.float64.

## Pérdida de Significancia en la función Ln y Exp

Cómo mencioné anteriormente, se busca encontrar la pérdida de significancia que puede ocurrir en la siguiente propiedad: 

                            Ln(exp^(x)) = x
                            
Se buscó que se cumpliera esa propiedad para cada tipo de lista (16,32,64), llevándolas primero a su función exponencial y luego al correspondiente logaritmo natural, buscando el error que se da entre el número original (x) y el valor de la propiedad.

## Resultados

Los resultados obtenidos, se graficaron y se puede observar que dicho error existe, y que para 16 el error es mucho mayor al de 32 y 64, lo curioso es que el error de 32 es menor al de 64 en un comienzo, pero a medida que los decimales aumentan este error se invierte. 

![alt text](https://github.com/meechaguep/MCOC-Proyecto-0/blob/master/loss-of-significance.png?raw=true)
