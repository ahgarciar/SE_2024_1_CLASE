
import serial as s #pyserial...

#arduino = s.Serial(baudrate=9600, port= "COM5", timeout=1)  #windows
arduino = s.Serial(baudrate=9600, port= "/dev/cu.usbmodem1301", timeout=1)  #mac

print("conexion existosa")

lineas_to_leer = 10 #n lineas...
cont = 0

archivo = open("../Archivos/archivo_numeros.csv", "w") #crea un archivo en el que se escribira informacion

while cont < lineas_to_leer:
    cadena = arduino.readline() # b'Hola Clase de Sistemas Embebidos Chidos!\r\n'
    cadena = cadena.decode()
    cadena =  cadena.replace("\r","")
    cadena = cadena.replace("\n", "")
    if  cadena != "":
        print(cadena)
        archivo.write(cadena + "\n")
    cont += 1
archivo.flush()
archivo.close()

