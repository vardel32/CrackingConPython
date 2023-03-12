import pyperclip
#casdena para cifrar/descifrar
mensaje = 'f2? 81 3r552 38yt262 s8z2 ? 7262'
#mensaje = 'Soy un perro pulgoso fumo y toso'
#Clave para el cifrado/descifrado
clave = 13
#modo del programa
modo = 'descifrar'
#Establecer como 'encriptar' o 'desencriptar'
#Todos los posibles simbolos que se pueden descifrar
simbolos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
#Se almacena de forma cifrada/descifrada el mensaje
traducido = ''
for simbolo in mensaje:
    #Solo los simbolos de la cadena 'simbolos' se pueden cifrar//descifrar
    if simbolo in simbolos:
        simboloIndice = simbolos.find(simbolo)
        #Se realiza el cifrado descifrado
        if modo == 'cifrar':
            indiceTraducido = simboloIndice + clave
        elif modo == 'descifrar':
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
print('\nMensaje cifrado: '+mensaje+'\n')
print('\nMensaje descifrado: '+traducido+'\n')
pyperclip.copy(traducido)