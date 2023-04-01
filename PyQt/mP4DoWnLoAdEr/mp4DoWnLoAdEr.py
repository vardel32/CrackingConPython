from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from pytube import YouTube


class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent=parent)

        # Se establece el tamanio de la ventana
        self.setFixedSize(300, 300)
        self.setWindowTitle("mp4 DoWnLoAdEr")

        # Boton
        self.button = QPushButton("Descargar MP4", self)
        self.button.setGeometry(50, 120, 200, 30)
        self.button.clicked.connect(self.descargar)

        # Entrada de texto
        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(50, 80, 200, 30)

        # Labels
        self.label_url = QLabel("URL", self)
        self.label_url.setGeometry(135, 40, 200, 30)
        self.label_estado = QLabel("", self)
        self.label_estado.setGeometry(20, 150, 200, 30)

        self.label_firma = QLabel("- insoportable -", self)
        self.label_firma.setGeometry(110, 230, 200, 30)


    def descargar(self):
        url = self.text_input.text()
        mp3 = YouTube(url).streams.get_audio_only()
        mp3.download()
        self.label_estado.setText(mp3.default_filename)


if __name__ == '__main__':
    # Inicia la aplicacion
    app = QApplication([])
    # Crea la ventana
    window = MainApp()
    # Muestra la ventana
    window.show()
    # Ejecuta la aplicacion
    app.exec_()
