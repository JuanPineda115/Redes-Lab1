#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
import socket, pickle, bitarray
from random import randint, seed

HOST = "127.0.0.1"  
PORT = 65431      

#capa de ruido (client):
#Añade ruido al mensaje del usuario
# y Serializa el mensaje con Pickle para ser enviado
def addNoise(message):
    bitlist = bitarray.bitarray()
    bitlist.frombytes(message.encode('utf-8'))
    #agregar el ruido
    for j in bitlist:
        seed(bytearray(message, 'utf-8'))
        #115 es el numero favorito de Pineda y siempre busca referenciarlo
        odds = randint(15,115)
        #probabilidad de 1% de realizar un cambio de bit
        if(odds == 115):
            if(j == 1):
                bitlist[bitlist.index(j)]  = 0
            elif(j == 0):
                bitlist[bitlist.index(j)] = 1
    bitlist = pickle.dumps(bitlist)
    return bitlist


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        userMessage = input("Ingrese su mensaje: ")
        finalMessage = addNoise(userMessage)
        #serializamos el mensaje con pickle al enviarlo
        s.sendall(finalMessage)
