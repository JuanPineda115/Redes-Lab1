#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
import socket
import random

HOST = "127.0.0.1"  
PORT = 65432      

def addNoise(message):
    bytesMessage = bytearray(message, 'ASCII')
    print('antes del ruido', message)
    #agregar el ruido
    for j in bytesMessage:
        print(j)
        odds = random.randint(1,10)
        if(odds == 1):
            #si j es mayor a 200 le restaremos al valor ascii hasta un maximo de 255 para dejarlo en 0 en caso de salir ese codigo
            if(j >= 93):
                offset = random.randint(1, 28)
                print('si hace algo el offset?', offset)
                bytesMessage[bytesMessage.index(j)] -= offset
            #si j es menor a 200, le sumaremos al valor ascii hasta un maximo de 56 para dejarlo en 255 en caso de salir 199
            elif(j < 93):
                offset = random.randint(1, 28)
                print('si hace algo el offset?', offset)
                bytesMessage[bytesMessage.index(j)] += offset
    print('despues del ruido', bytesMessage)
    #ya que el mensaje quedo como un array, lo juntamos en bytes
    return bytesMessage

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        userMessage = input("Ingrese su mensaje: ")
        finalMessage = addNoise(userMessage)
        s.sendall(finalMessage)
