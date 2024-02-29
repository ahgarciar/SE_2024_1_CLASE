
import serial as s #pyserial...

#arduino = s.Serial(baudrate=9600, port= "COM5", timeout=1)  #windows
arduino = s.Serial(baudrate=9600, port= "/dev/cu.usbmodem1301", timeout=1)  #mac

print("conexion existosa")


