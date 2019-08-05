

import numpy as np
from numpy import *
from matplotlib import pyplot
from matplotlib import pyplot as plt
import scipy as sp
import pylab

#creo listas de ceros con la respectiva cantidad de bits que quiero trabajar
lista16= np.zeros((6), dtype=np.float16)
lista32 = np.zeros((6), dtype=np.float32)
lista64 = np.zeros((6), dtype=np.float64)
largolistas= len(lista32)

#esta lista la utilizare como base con la idea de ir aumentando la cantidad de decimales
listaX=[0.1,0.11,0.111,0.1111,0.11111,0.111111]
elemento=0

print "La lista siguiente corresponde a la lista original"
print listaX

#Cuando hablo de elemento me refiero al numero dentro de cada lista
while elemento < largolistas:
	lista16[elemento]=listaX[elemento]
	lista32[elemento]=listaX[elemento]
	lista64[elemento]=listaX[elemento]
	elemento +=1 

exp16=[] 
for elemento in lista16:
	elemento= math.exp(elemento)
	exp16.append(elemento)

exp32=[]
for elemento in lista32:
	elemento= math.exp(elemento)
	exp32.append(elemento)

exp64=[]
for elemento in lista64:
	elemento= math.exp(elemento)
	exp64.append(elemento)
print "\n"
print "A continuacion se presentan el valor de la lista con su funcion exponencial dependiendo el tipo de float 16,32,64"
print "\n"
print "Lista exponencial float16"
print exp16
print "\n"
print "Lista exponencial float32"
print exp32
print "\n"
print "Lista exponencial float64"
print exp64


ln16=[] 
for elemento in exp16:
	elemento= math.log(elemento)
	ln16.append(elemento)

ln32=[]
for elemento in exp32:
	elemento= math.log(elemento)
	ln32.append(elemento)


ln64=[]
for elemento in exp64:
	elemento= math.log(elemento)
	ln64.append(elemento)
print "\n"
print "ln de las listas"
print "\n"
print "Lista Ln a la exponencial float16"
print ln16
print "\n"
print "Lista Ln a la exponencial float32"
print ln32
print "\n"
print "Lista Ln a la exponencial float64"
print ln64
print "\n"
error16 =[]
error32 =[]
error64 =[]
elemento = 0
while elemento < largolistas:
    error16.append((abs(lista16[elemento] - ln16[elemento]))/lista16[elemento])
    error32.append((abs(lista32[elemento] - ln32[elemento]))/lista32[elemento])
    error64.append((abs(lista64[elemento] - ln64[elemento]))/lista64[elemento])
    elemento+=1

print "Los errores se presentan a continuacion, siendo comparados al valor inicial dado"
print "\n"
print "Error float16"
print error16
print "\n"
print "Error float32"
print error32
print "\n"
print "Error float64"
print error64

print "El grafico es el siguiente"



pyplot.plot(listaX,error16, "b",label="Float 16" )
pyplot.plot(listaX,error32,"r" ,label="Float 32")
pyplot.plot(listaX,error64,"g",label="Float 64")

pyplot.xlabel("Lista original, aumentan decimales")
pyplot.ylabel("Error propiedad ln(exp(x))=x ")
pylab.legend(loc='uper right')

plt.show()

	