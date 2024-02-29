
lecturaSensor = "230,240,235,250" #promedio, mediana, valorMayor, valorMenor

datos = lecturaSensor.split(",")
print(datos) # ["230", "240", "235", "250"]

datos_numericos = [float(i) for i in datos]
print(datos_numericos)

valProm = []
valMediana = []
valMayor = []
valMenor = []

valProm.append(datos_numericos[0])
valMediana.append(datos_numericos[1])
valMayor.append(datos_numericos[2])
valMenor.append(datos_numericos[3])

#generaron 4 archivos.... uno por lista. :D!
