#Primera prueba de la libreria Pytube
#La idea de este código fuente
#es que se pueda descargar un video en formato de mp3 desde YouTube.
#25/03/2023


#La libreria se instala mediante 'pip install pytube'
from pytube import YouTube
import os

#URL del video de YouTube
url = 'https://www.youtube.com/watch?v=vm022BE7dgM'

#download_folder = os.path.expanduser('~/Videos')
#print(download_folder)

#Se crea una instancia del objeto YouTube y se obtiene la mejor resolucion
cancion = YouTube(url).streams.get_audio_only()

cancion.download()
#print(download_folder)
print(cancion.default_filename)