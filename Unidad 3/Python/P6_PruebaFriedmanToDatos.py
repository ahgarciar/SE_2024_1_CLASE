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

#Friedman Test
from scipy import stats
res = stats.friedmanchisquare(datosPromedio, datosMediana, datosValMenor)
#Ho = hipotesis nula...
# NO EXISTE DIFERENCIA ESTADISTICA ENTRE LAS MUESTRAS (GRUPOS)
#Ha = hipostesis alternativa
# EXISTE DIFERENCIA ESTADISTICA ENTRE LAS MUESTRAS (GRUPOS)
#EVALUACION DE LA PRUEBA....Si pvalue < 0.05 se rechaza Ho y se acepta Ha
# SI pvalue >= 0.05 se acepta Ho y se rechaza Ha
print(res)
