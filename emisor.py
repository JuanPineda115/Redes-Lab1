#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
import socket, pickle
from bitarray import *
from noiseLayer import *
from random import randint, seed

HOST = "127.0.0.1"  
PORT = 65431      



key = "1101"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #conexion del socket
    s.connect((HOST, PORT))
    #ciclo while para enviar todos los mensajes sin ejecutar varias veces
    while True:
        userMessage = input("Ingrese su mensaje: ")
        processMessage = addNoise(userMessage)
        noisedMessage = bitlist_to_s(processMessage)
        finalMessage = encodeData(processMessage.tobytes().decode('utf-8'), key)
        print(finalMessage)
        s.sendall(finalMessage)