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
def addNoise(message):
    binary = ' '.join(format(ord(x), 'b') for x in message)
    bitlist = []
    for j in binary:
        bitlist.append(j)
    #agregar el ruido
    print("pre-noised", binary)
    noiseArray = []
    final = []
    limpio = ""
    for j in bitlist:
        odds = randint(1,50)
        if(odds == 1):
            if(j == '1'):
                noiseArray.append(0)
            elif(j == '0'):
                noiseArray.append(1)
        else:
            if(j != ' '):
                noiseArray.append(j)

        
    #ya que el mensaje quedo como un array, lo juntamos en bytes
    noisedMessage = ''.join(str(x) for x in noiseArray)
    print("pos-noised", noisedMessage)
    return noisedMessage


#capa de ruido (host):
#Recibe el dato crudo y lo carga con pickle
# Limpia el mensaje en caso de ser interrumpido por ruido.
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

