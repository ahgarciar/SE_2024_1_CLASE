
#archivo = open("./archivo_numeros.csv")
archivo = open("../Archivos/archivo_numeros.csv")

contenido = archivo.readlines()

##print(contenido)

lista_numeros = []

for linea in contenido:
    lista_numeros.append(int(linea))

print(lista_numeros)