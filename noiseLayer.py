#Universidad del valle de Guatemala
#Redes
#Diego Crespo 19541
#Juan Pablo Pineda 19087


import bitarray
from random import seed, randint
import pickle





#capa de ruido (client):
#Añade ruido al mensaje del usuario
# y Serializa el mensaje con Pickle para ser enviado

def bitlist_to_chars(bl):
    bi = iter(bl)
    bytes = zip(*(bi,) * 8)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    for byte in bytes:
        yield chr(sum(bit << s for bit, s in zip(byte, shifts)))
    
def bitlist_to_s(bl):
        return ''.join(bitlist_to_chars(bl))


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
    # bitlist = pickle.dumps(bitlist)
    return bitlist


#capa de ruido (host):
#Recibe el dato crudo y lo carga con pickle
# Limpia el mensaje en caso de ser interrumpido por ruido.

def supressNoise(message):
    #Carga el mensaje con pickle y lo pasa a bytes
    received = pickle.loads(message)
    #TODO Limpieza del mensaje
    return received



#CRC ALGORITHM
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0 : pick]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else: # If leftmost bit is '0'
            tmp = xor('0'*pick, tmp) + divident[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    checkword = tmp
    return checkword
 
def encodeData(data, key):

    l_key = len(key)

    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)

    codeword = data + remainder
    return pickle.dumps(codeword)

