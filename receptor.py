#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087
import socket


HOST = "127.0.0.1" 
PORT = 65432       

def BinarytoString(binary):
    binary_int = int(binary,2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return ascii_text;


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Conexion Entrante del puerto(proceso) {addr}")
        while True: 
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recibido: {data}")
            conn.sendall(data)