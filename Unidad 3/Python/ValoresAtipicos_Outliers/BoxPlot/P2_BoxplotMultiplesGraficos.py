
import matplotlib.pyplot as plt 

datos1=[108, 31, 75, 87, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]
datos2=[180, 31, 75, 190, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]

datos =[datos1, datos2]

plt.boxplot(datos, labels=["Grafica 1", "Grafica 2"])

plt.title("Boxplot Multiples Graficas")
plt.show()


