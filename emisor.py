#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
import socket

HOST = "127.0.0.1"  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #agregar un ciclo while para enviar varios mensajes
    s.connect((HOST, PORT))
    #agregar la capa de ruido antes de hacer el envio 
    s.sendall(b"enviando datos al receptor :)")
