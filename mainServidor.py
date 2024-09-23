import numpy as np
from PIL import Image
import socket
import pickle
import time
import random

import steganography as stgn
import steganographyStats as stgns
import statistics as stats

image_route_in = "Lenna.png"
image_route_out = "out.png"
# image_route_out_stats = "outStats.png"
message_01 = "hello"
message_02 = "En contraste, las «microproposiciones» son los elementos coadyuvantes de la cohesión de un texto, pero a nivel más particular o local. Esta distinción fue realizada por Teun van Dijk en 1980.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Las ideas que comunica un texto están contenidas en lo que se suele denominar «macroproposiciones», unidades estructurales de nivel superior o global, que otorgan coherencia al texto constituyendo su hilo central, el esqueleto estructural que cohesiona elementos lingüísticos formales de alto nivel, como los títulos y subtítulos, la secuencia de párrafos, etc. En contraste, las «microproposiciones» son los elementos coadyuvantes de la cohesión de un texto, pero a nivel más particular o local. Esta distinción fue realizada por Teun van Dijk en 1980.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original.En contraste, las «microproposiciones» son los elementos coadyuvantes de la cohesión de un texto, pero a nivel más particular o local. Esta distinción fue realizada por Teun van Dijk en 1980.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Las ideas que comunica un texto están contenidas en lo que se suele denominar «macroproposiciones», unidades estructurales de nivel superior o global, que otorgan coherencia al texto constituyendo su hilo central, el esqueleto estructural que cohesiona elementos lingüísticos formales de alto nivel, como los títulos y subtítulos, la secuencia de párrafos, etc. En contraste, las «microproposiciones» son los elementos coadyuvantes de la cohesión de un texto, pero a nivel más particular o local. Esta distinción fue realizada por Teun van Dijk en 1980.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original."
T = 10
# Tmin = 10
# Tmax = 20
# seed = 0
# n = 30

# stgn.stgn_in(image_route_in,message_01,T)
# print(stgn.stgn_out(image_route_out,T))
# stats.histogramDifference(image_route_out,n)

# stgns.stgn_in(image_route_in,message_02,Tmin,Tmax,seed)
# print(stgns.stgn_out(image_route_out_stats,Tmin,Tmax,seed))
# stats.histogramDifference(image_route_out_stats,n)'''

def receiveData(host='192.168.0.10', port=23):
    # Creación del socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f'Servidor escuchando en {host}:{port}')

    while True:
        # Aceptar la conexión del cliente
        client_socket, client_address = server_socket.accept()
        print(f'Conexión aceptada de {client_address}')

        try:
            # Registrar el tiempo de recepción
            start_time = time.time()
            # Recibir y mostrar los datos
            data = b''
            while True:
                chunk = client_socket.recv(4096)  # Recibir datos en fragmentos de 4096 bytes
                if not chunk:
                    break
                data += chunk

            # Registrar el tiempo después de recibir los datos
            end_time = time.time()

            # Tiempo transcurrido
            elapsed_time = end_time - start_time

            # Imprimir los datos recibidos
            print(f'Datos recibidos: {data[:100]}...')  # Mostrar solo los primeros 100 bytes para no saturar la salida
            print(len(data))

            # Impresion del tiempo transcurrido
            print(f'Tiempo de envio: {elapsed_time} segundos')

            # Deserialización de los datos
            # vecdeser = pickle.loads(data)

        finally:
            # return vecdeser
            return data
            client_socket.close()

data = receiveData()
print("Data")
print(data)

with open('LennaRestaured.png', 'wb') as f:
    f.write(data)

print(stgn.stgn_out('LennaRestaured.png',T))