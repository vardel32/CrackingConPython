import sys
import pyperclip
#cadena para cifrar/descifrar
print('\nIntroduce el mensaje:\n')
mensaje = input()

#Clave para el cifrado/descifrado
print('Introduce la clave:')
clave = int(input())

#modo del programa
print('Introduce el modo del programa eligiendo un numero:\n1- cifrar\n2- descifrar')
modo = int(input())
#Establecer como 'cifrar' o 'descifrar'
if(modo != 1 and modo != 2):
    print('Modo de programa no valido.')
    sys.exit()

#Todos los posibles simbolos que se pueden descifrar
simbolos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
#Se almacena de forma cifrada/descifrada el mensaje
traducido = ''
for simbolo in mensaje:
    #Solo los simbolos de la cadena 'simbolos' se pueden cifrar//descifrar
    if simbolo in simbolos:
        simboloIndice = simbolos.find(simbolo)
        #Se realiza el cifrado descifrado
        if modo == 1:
            indiceTraducido = simboloIndice + clave
        elif modo == 2:
            indiceTraducido = simboloIndice - clave

        #Se maneja la envoltura
        if indiceTraducido >= len(simbolos):
            indiceTraducido = indiceTraducido - len(simbolos)
        elif indiceTraducido <0:
            indiceTraducido = indiceTraducido + len(simbolos)

        traducido = traducido + simbolos[indiceTraducido]
    else:
        #Agregar simbolo sin cifrar/descifrar
        traducido = traducido + simbolo
        
#Se muestra la cadena traducido
print('\nMensaje: '+mensaje+'\n')
if(modo == 1):
    print('\nMensaje cifrado: '+traducido+'\n')
else:
    print('\nMensaje descifrado: '+traducido+'\n')
pyperclip.copy(traducido)