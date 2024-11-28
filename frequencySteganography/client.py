"""
Envío de imágenes esteganográficas
(Cliente)
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías
# ------------------------------------------------------------------------------------------------------------------

import socket
import pickle

# ------------------------------------------------------------------------------------------------------------------
# Funciones
# ------------------------------------------------------------------------------------------------------------------

def sendData(data1, data2, data3 , host = '192.168.0.10', port = 8080):

    # Crear el socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        # Enviar los datos
        data1_ = sendText (data1)
        client_socket.sendall(data1_)

        # Envío de un dato de separación (valor = b'\x00x98')
        client_socket.sendall(b'\x00x98')

        data2_ = sendText (data2)
        client_socket.sendall(data2_)
        
        client_socket.sendall(b'\x00x98')

        data3_ = sendArray(data3)
        client_socket.sendall(data3_)

        client_socket.sendall(b'\x00x98')

        print('Datos enviados')

    finally:
        client_socket.close()

def sendText (textFile):
    with open(textFile, 'rb') as f:
        binaryData = f.read()
        return binaryData

def sendArray (array):
    # Serializar el arreglo
    data = pickle.dumps(array)
    return data
