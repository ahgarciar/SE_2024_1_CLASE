
import matplotlib.pyplot as plt 

datos1=[108, 31, 75, 87, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]
datos2=[180, 31, 75, 190, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]

datos =[datos1, datos2]


# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2, 2, figsize=(8, 4)) #rows, columns
#

#BOXPLOT DEFAULT  => WHIS 1.5
axis[0, 0].boxplot(datos, labels=["Grafica 1", "Grafica 2"])
axis[0, 0].set_title("Boxplot DEFAULT")
#

#BOXPLOT WHIS 1.5
axis[0, 1].boxplot(datos, labels=["Grafica 1", "Grafica 2"], whis = 1.5)
axis[0, 1].set_title("Boxplot Whis de 1.5")
#

#BOXPLOT WHIS 3.0
axis[1, 0].boxplot(datos, labels=["Grafica 1", "Grafica 2"], whis = 3.0)
axis[1, 0].set_title("Boxplot Whis de 3.0")
#

#BOXPLOT WHIS 4.0
axis[1, 1].boxplot(datos, labels=["Grafica 1", "Grafica 2"], whis = 4.0)
axis[1, 1].set_title("Boxplot Whis de 4.0")
#

plt.show()

