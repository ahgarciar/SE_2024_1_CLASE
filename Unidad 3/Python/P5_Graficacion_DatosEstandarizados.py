
archivo = open("../Archivos/datosPromEstandarizados.csv")
contenido = archivo.readlines()
print(contenido)

datos = [float(i) for i in contenido]
print(datos)

from matplotlib import pyplot  #pip install matplotlib

y = datos
x = [i for i in range(len(datos))]
print(x)

pyplot.plot(x, y)
pyplot.show()