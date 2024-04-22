
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec

datos1=[108, 31, 75, 87, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]
datos2=[180, 31, 75, 190, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]

datos =[datos1, datos2]


# Create 2x2 sub plots
gs = gridspec.GridSpec(2, 2)

plt.figure(figsize=(12, 7))

ax = plt.subplot(gs[0, :]) # row 0, span all columns
plt.boxplot(datos, labels=["Grafica 1", "Grafica 2"])
plt.title("Boxplot DEFAULT")

ax = plt.subplot(gs[1, 0]) # row 1, col 0
plt.boxplot(datos, labels=["Grafica 1", "Grafica 2"], whis = 1.5)
plt.title("Boxplot Whis de 1.5")

ax = plt.subplot(gs[1, 1]) # row 1, col 1
plt.boxplot(datos, labels=["Grafica 1", "Grafica 2"], whis = 3.0)
plt.title("Boxplot Whis de 3.0")

plt.show()

