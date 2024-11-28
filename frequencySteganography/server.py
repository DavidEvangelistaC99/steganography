"""
Envío de imágenes esteganográficas
(Servidor)
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías
# ------------------------------------------------------------------------------------------------------------------

import socket
import time
import pickle

# ------------------------------------------------------------------------------------------------------------------
# Funciones
# ------------------------------------------------------------------------------------------------------------------

def receiveData(text1, text2, host = '192.168.0.10', port = 8080):

    # Creación del socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor esperando conexión...")
    conn, addr = server_socket.accept()
    print(f'Servidor escuchando en ({host}:{port})')

    buffer = b''
    count = 0
    data1, data2, data3 = b'', b'', b''

    # Tiempo de inicio
    start_time = time.time()  

    while True:

        chunk = conn.recv(2048)
        if not chunk:
            break

        buffer += chunk

        while b'\x00x98' in buffer:

            # Valor de separación (valor = b'\x00x98')
            data, buffer = buffer.split(b'\x00x98', 1)
            count += 1

            if count == 1:
                data1 = data
                getTxt(text1, data1)
            elif count == 2:
                data2 = data
                getTxt(text2, data2)
            elif count == 3:
                data3 = data
                # Tiempo de finalización
                end_time = time.time() 

                # Deserializar el arreglo
                array = pickle.loads(data3)
                print(f"Datos recibidos en {end_time - start_time:.2f} segundos")

                break
    
    # Si Y es comprimida no consideramos el return
    return array

def getTxt (name, data):
    with open(name, 'w') as f:
        f.write(data.decode('utf-8'))
