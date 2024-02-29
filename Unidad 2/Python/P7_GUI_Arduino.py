import serial as conecta  #arduino..... pyserial
import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P7_GUI_Arduino.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.txt_puerto.setText("/dev/cu.usbmodem11301")

        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)  ##lecuta de datos de arduino

        self.btn_control_led.setText("PRENDER")  # ENVIAR CADENA ACTUADORES
        self.btn_control_led.clicked.connect(self.control_led)
        # self.btn_control_led.setEnabled(False)

        self.cont = 1

    # Área de los Slots
    def control_led(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                self.arduino.write(str(self.cont).encode())
                self.cont += 1

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
