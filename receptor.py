#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
import socket, pickle, bitarray
from noiseLayer import *
from Hamming import *



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
            #captura de datos
            package = pickle.loads(data)
            received = package[0].decode('utf-8')
            #hamming
            x = len(received)
            r = package[1]
            err = detectError(received, r)
            if (received[-1]=='0'):
                print(received)
                print("No existe un error")
            else:
                print(received)
                print("Existe un error")
