import serial as conecta  #arduino..... pyserial
import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P12_GUI_Arduino.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.txt_puerto.setText("/dev/cu.usbmodem1401")

        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)  ##lecuta de datos de arduino

        self.datosToGuardar = 10
        self.contArchivo = 1
        self.datos = [] #contiene los datos temporales

    # Área de los Slots
    def accion(self):  # conecta/desconecta/reconecta vinculo con arduino
        try:
            txt_btn = self.btn_accion.text()
            if txt_btn == "CONECTAR":  ##arduino == None
                self.txt_estado.setText("CONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                puerto = self.txt_puerto.text()
                # puerto = "COM" + self.txt_puerto.text() #alternativa
                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                self.segundoPlano.start(10)
            elif txt_btn == "DESCONECTAR":
                self.txt_estado.setText("DESCONECTADO")
                self.btn_accion.setText("RECONECTAR")
                self.segundoPlano.stop()
                self.arduino.close()
            else:  # RECONECTAR
                self.txt_estado.setText("RECONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                self.arduino.open()
                self.segundoPlano.start(10)
        except Exception as error:
            print(error)
        # self.arduino.isOpen()

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                if self.arduino.inWaiting():
                    # leer
                    cadena = self.arduino.readline().decode()
                    cadena = cadena.replace("\r", "")
                    cadena = cadena.replace("\n", "")
                    # print(variable)
                    if not cadena == "":
                        self.lw_datos.addItem(cadena)
                        self.lw_datos.setCurrentRow(self.lw_datos.count() - 1)

                        if self.datosToGuardar > 0: #guarda los datos temporales
                            self.datos.append(cadena)
                            self.datosToGuardar -= 1
                        else: #construye el archivo
                            archivo = open("../DatosSensorPotenciometro/archivo_" + str(self.contArchivo) + ".csv", "w")
                            for dato in self.datos:
                                archivo.write(dato)
                                archivo.write("\n")
                            archivo.flush()
                            archivo.close()
                            self.contArchivo += 1
                            self.datosToGuardar = 10

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
