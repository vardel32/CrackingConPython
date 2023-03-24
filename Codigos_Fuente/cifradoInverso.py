#Cifrado inverso 
# - 11/03/2023
# - Varto
#En este programa se observan los siguientes temas
#   Funcion len()
#   Bucles while
#   Oepradores de comparacion
#   Tipos de datos booleanos
#   Condiciones
#   Bloques
print('\nIntroduce el mensaje a cifrar:')
mensaje = input()
traduccion =''

largoDelMensaje = len(mensaje)-1
#La expresion evaluada y almacenada en la variable es len(mensaje)-1
#   la funcion len admite un argumento de tipo string 
#   y devuelve un valor entero de cuantos caracteres hay en la cadena.
#   es decir, la longitud de la cadena
#   Se resta 1 pues los indices de las cadenas comienzan en 0.

while largoDelMensaje >= 0:
    traduccion = traduccion + mensaje[largoDelMensaje]
    largoDelMensaje = largoDelMensaje - 1
#Mientras el largo del mensaje sea igual o mayor a cero 
#el ciclo while continuará ejecutandose.
#En este caso el cifrado inverso ocurre dentro de este ciclo.
#Mediante la variable 'largoDelMensaje' se obtienen 
#los caracteres del mensaje en orden inverso
#es decir desde el final de la cadena hasta el inicio
# en cada iteracion último caracter es tomado y colocado
#dentro de la variable 'traduccion'
#El largo del mensaje se modifica para indicar la posicion
#del siguiente caracter que se debe tomar

print('\nMensaje cifrado:\n'+traduccion+'\n')