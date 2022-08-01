#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
import socket
import random

HOST = "127.0.0.1"  
PORT = 65432      

def addNoise(message):
    #primero hacemos encoding a ASCII
    bytesMessage = bytearray(message, 'ASCII')
    for j in bytesMessage:
        #probabilidades del 10% de que la letra sea alterada
        odds = random.randint(1,10)
        if(odds == 1):
            #Si el codigo ascii es muy alto se le restara un offset para que no se pase del limite
            if(j >= 93):
                #offset random
                offset = random.randint(1, 28)
                #aplicamos el offset
                bytesMessage[bytesMessage.index(j)] -= offset
            #si el codigo ascii de la letra es muy bajo, se le sumara para que no se quede un numero negativo o 0
            elif(j < 93):
                #offset random
                offset = random.randint(1, 28)
                #aplicamos el offset
                bytesMessage[bytesMessage.index(j)] += offset
    return bytesMessage

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #conexion del socket
    s.connect((HOST, PORT))
    #ciclo while para enviar todos los mensajes sin ejecutar varias veces
    while True:
        userMessage = input("Ingrese su mensaje: ")
        finalMessage = addNoise(userMessage)
        s.sendall(finalMessage)
