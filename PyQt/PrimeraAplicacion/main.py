from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        #Se establece un tamaño fijo de 500x500
        self.setFixedSize(500, 500)
        self.setWindowTitle("Primera App")

        #Se obtienen las dimensiones de las ventanas
        largo = self.frameGeometry().width()
        alto = self.frameGeometry().height() #se obtiene la resolucion de la ventana

        #Se crea una instancia label
        label = QLabel("Puro pinche VOLUMES", self)
        #Se debe establecer en que widget se quiere mostrar el label
        #Con la etiqueta self se indica que debe de ir dentro del widger actual

        #Se define la posicion de la etiqueta
        label.setGeometry(0, 0, largo, alto)
        #Los parametros son:
        #Posicion de izq a der, posicion de arriba a abajo, largo, altura
        #Se coloca un fondo negro con letra blanca
        label.setStyleSheet("background:#424242; color:#fff")
        #Las posiciones y tamanios se manejan en pixeles


if __name__ == '__main__':
            #Solo se declara una sola vez la qapplication
            #Inicia la aplicacion
    app = QApplication([])
            #Se crea una ventana
            #Se establece como ventana principal
    window = MainApp()
            #Se muestra la ventana
            #Por default las ventanas estan ocultas
    window.show()
            #Se ejecuta la aplicacion
    app.exec_()
