from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

global modo
global clave
class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent=parent)

        # Se establece un tamaño fijo de 500x500
        self.setFixedSize(500, 200)
        self.setWindowTitle("Cifrado César")

        # Label
        self.label = QLabel("*Mensaje traducido*", self)
        self.label.setGeometry(20, 20, 200, 30)

        # Botón
        self.button = QPushButton("Traducir", self)
        self.button.setGeometry(20, 60, 120, 30)
        self.button.clicked.connect(self.traducir)

        # Entrada de texto
        self.text_input1 = QLineEdit(self)
        self.text_input1.setGeometry(20, 100, 200, 30)

        # Crear una QComboBox
        self.combobox = QComboBox(self)
        self.combobox.setGeometry(230, 100, 150, 30)

        # Agregar opciones a la combobox
        self.combobox.addItem("1")
        self.combobox.addItem("2")
        self.combobox.addItem("3")
        self.combobox.addItem("4")
        self.combobox.addItem("5")
        self.combobox.addItem("6")
        self.combobox.addItem("7")
        self.combobox.addItem("8")
        self.combobox.addItem("9")
        self.combobox.addItem("10")
        self.combobox.addItem("11")
        self.combobox.addItem("12")
        self.combobox.addItem("13")
        self.combobox.addItem("14")
        self.combobox.addItem("15")
        self.combobox.addItem("16")

        # Conectar la señal "currentIndexChanged" de la combobox a la función que actualizará el QLabel
        self.combobox.currentIndexChanged.connect(self.update_label)

        # Radiobutton
        self.radio_button1 = QRadioButton("Cifrar", self)
        self.radio_button1.setGeometry(20, 140, 100, 30)

        self.radio_button2 = QRadioButton("Descifrar", self)
        self.radio_button2.setGeometry(20, 160, 100, 30)

        self.radio_button1.clicked.connect(self.cifrar)
        self.radio_button2.clicked.connect(self.descifrar)
        # Variables de instancia
        self.modo = 1
        self.clave = 1

    def traducir(self):
        global modo, clave  # <--- No es necesario usar "global" aquí ya que ya se han definido como variables de instancia en __init__
        mensaje = self.text_input1.text()

        # Todos los posibles simbolos que se pueden descifrar
        simbolos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
        # Se almacena de forma cifrada/descifrada el mensaje
        traducido = ''
        for simbolo in mensaje:
            # Solo los simbolos de la cadena 'simbolos' se pueden cifrar//descifrar
            if simbolo in simbolos:
                simboloIndice = simbolos.find(simbolo)
                # Se realiza el cifrado descifrado
                if self.modo == 1:  # <--- Usar "self.modo" en lugar de "modo"
                    indiceTraducido = simboloIndice + self.clave  # <--- Usar "self.clave" en lugar de "clave"
                elif self.modo == 2:  # <--- Usar "self.modo" en lugar de "modo"
                    indiceTraducido = simboloIndice - self.clave  # <--- Usar "self.clave" en lugar de "clave"

                # Se maneja la envoltura
                if indiceTraducido >= len(simbolos):
                    indiceTraducido = indiceTraducido - len(simbolos)
                elif indiceTraducido < 0:
                    indiceTraducido = indiceTraducido + len(simbolos)

                traducido = traducido + simbolos[indiceTraducido]
            else:
                # Agregar simbolo sin cifrar/descifrar
                traducido = traducido + simbolo

        self.label.setText(traducido)

    def cifrar(self):
        self.modo = 1  # <--- Usar "self.modo" en lugar de "modo"

    def descifrar(self):
        self.modo = 2  # <--- Usar "self.modo" en lugar de "modo"

    def update_label(self):
        # Obtener el texto de la opción seleccionada en la combobox
        self.clave = int(self.combobox.currentText())  # <--- Usar "self.clave" en lugar de "clave"

if __name__ == '__main__':
    # Inicia la aplicación
    app = QApplication([])
    # Crea la ventana principal
    window = MainApp()
    # Muestra la ventana
    window.show()
    # Ejecuta la aplicación
    app.exec_()
