import math

archivo = open("../Archivos/datos_PromedioLectura.csv")
contenido = archivo.readlines()
print(contenido)

datos = [float(i) for i in contenido]
print(datos)

prom = sum(datos)/len(datos)
print("Promedio: " + str(prom))

varianza = 0
for dato in datos:
    varianza += math.pow(dato-prom,2)
varianza = varianza/len(datos)
print("Varianza: " + str(varianza))

desvEstandar = math.sqrt(varianza)
print("Desviacion E.: " + str(desvEstandar))

datos_estandarizados = []
for dato in datos:
    #print(dato)
    d_stand = (dato - prom) / desvEstandar
    d_stand = round(d_stand, 2)
    datos_estandarizados.append(d_stand)
print(datos_estandarizados)

archivoNuevo = open("../Archivos/datosPromEstandarizados.csv", "w")
for i in datos_estandarizados:
    archivoNuevo.write(str(i) + "\n")
archivoNuevo.flush()
archivoNuevo.close()