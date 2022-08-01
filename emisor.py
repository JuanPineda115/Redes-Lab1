#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
from audioop import add
from email import message
from operator import index
import socket
from random import randint

HOST = "127.0.0.1"  
PORT = 65432      

def addNoise(message):
    binary = ' '.join(format(ord(x), 'b') for x in message)
    bitlist = []
    for j in binary:
        bitlist.append(j)
    #agregar el ruido
    noiseArray = []
    for j in bitlist:
        odds = randint(1,10)
        if(odds == 1):
            if(j == '1'):
                j  = 0
                noiseArray.append(j)
            elif(j == '0'):
                j = 1
                noiseArray.append(j)
        else:
            noiseArray.append(j)
    #ya que el mensaje quedo como un array, lo juntamos en bytes
    noisedMessage = ''.join(str(x) for x in noiseArray)
    return noisedMessage


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        userMessage = input("Ingrese su mensaje: ")
        finalMessage = addNoise(userMessage)
        s.sendall(bytes(finalMessage, 'ASCII'))
