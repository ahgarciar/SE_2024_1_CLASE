
archivo = open("../Archivos/datos_PromedioLectura.csv")
contenido = archivo.readlines()
print(contenido)

datos = [float(i) for i in contenido]
print(datos)

Xmin = min(datos)
Xmax = max(datos)

datos_normalizados = []
for dato in datos:
    #print(dato)
    d_norm = (dato - Xmin) / (Xmax-Xmin)
    d_norm = round(d_norm, 2)
    datos_normalizados.append(d_norm)
print(datos_normalizados)

archivoNuevo = open("../Archivos/datosPromNormalizados.csv", "w")
for i in datos_normalizados:
    archivoNuevo.write(str(i) + "\n")
archivoNuevo.flush()
archivoNuevo.close()