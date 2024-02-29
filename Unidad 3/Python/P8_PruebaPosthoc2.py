#Datos obtenidos desde arduino sin procesamiento adicional..
archivoDatosMediana = open("../Archivos/datos_MedianaLectura.csv")
archivoDatosPromedio = open("../Archivos/datos_PromedioLectura.csv")
archivoDatosValMenor = open("../Archivos/datos_ValorMenorLectura.csv")

contMediana = archivoDatosMediana.readlines()
contPromedio = archivoDatosPromedio.readlines()
contValMenor = archivoDatosValMenor.readlines()

datosMediana = [float(i) for i in contMediana]
datosPromedio = [float(i) for i in contPromedio]
datosValMenor = [float(i) for i in contValMenor]

print(datosMediana)
print(datosPromedio)
print(datosValMenor)

##
#LAS PRUEBAS POSTHOC TIENEN UTILIDAD SOLO CUANDO EXISTE UNA DIFERENCIA
#ESTADISTICA ENTRE LOS GRUPOS Y SE DESEA CONCOER AL GRUPO O GRUPOS
#QUE SON DIFERENTES
############################################################
import numpy as np
data = np.array([datosPromedio, datosMediana, datosValMenor])
############################################################

from scikit_posthocs import posthoc_conover_friedman
res = posthoc_conover_friedman(data.T)
print(res)
