
import serial as s #pyserial...

#arduino = s.Serial(baudrate=9600, port= "COM5", timeout=1)  #windows
arduino = s.Serial(baudrate=9600, port= "/dev/cu.usbmodem1301", timeout=1)  #mac

print("conexion existosa")

while True:
    cadena = arduino.readline() # b'Hola Clase de Sistemas Embebidos Chidos!\r\n'
    cadena = cadena.decode()
    cadena =  cadena.replace("\r","")
    cadena = cadena.replace("\n", "")
    if  cadena != "":
        valor = int(cadena)
        print(valor)


