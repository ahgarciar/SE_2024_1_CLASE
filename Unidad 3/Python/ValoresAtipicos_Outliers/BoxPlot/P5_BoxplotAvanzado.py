
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec

datos1=[108, 31, 75, 87, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]
datos2=[180, 31, 75, 190, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]

datos =[datos1, datos2]


# Create 2x2 sub plots
gs = gridspec.GridSpec(2, 2)
figure = plt.figure(figsize=(12, 7))

############################################################################################

############################################################################################

ax = figure.add_subplot(gs[0, :])
bp = ax.boxplot(datos, 
                patch_artist = True, # fill with color
                vert = False, # vertical box alignment
                labels=["Grafica 1", "Grafica 2"]) # will be used to label ticks
ax.set_title("Boxplot DEFAULT")

colors = ['lime', 'blue']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

############################################################################################

############################################################################################

ax = figure.add_subplot(gs[1, 0])
bp = ax.boxplot(datos, whis= 1.5, 
                patch_artist = True, # fill with color
                vert = False, # vertical box alignment
                labels=["Grafica 1", "Grafica 2"]) # will be used to label ticks
ax.set_title("Boxplot Whis de 1.5")

# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")

# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color ='red',
            linewidth = 2)

############################################################################################

############################################################################################

ax = figure.add_subplot(gs[1, 1])
bp = ax.boxplot(datos, whis= 3.0, 
                patch_artist = True, # fill with color
                vert = False, # vertical box alignment
                labels=["Grafica 1", "Grafica 2"]) # will be used to label ticks
ax.set_title("Boxplot Whis de 3.0")

# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='aqua',
               linewidth = 3)

# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='#e7298a',
              alpha = 0.5)

# x-axis labels
ax.set_yticklabels(['datos 1', 'datos 2'])

############################################################################################

plt.show()
{}

