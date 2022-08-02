#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
import socket, pickle, bitarray
from noiseLayer import *


HOST = "127.0.0.1" 
PORT = 65431






with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"{addr} Se ha conectado")
        while True: 
            data = conn.recv(1024)
            if not data:
                break
            #extraemos el mensaje con pickle
            received = supressNoise(data)
            #lo pasamos a bytes para mostrarlo adecuadamente
            print(f"{addr[1]} dice: {received}")
            conn.sendall(data)