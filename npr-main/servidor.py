"""
Imágenes decodificadas usando Deep Learning
INICTEL-2024
@dann_uc
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías
# ------------------------------------------------------------------------------------------------------------------

import socket
import pickle
import numpy as np
import importlib
keras = importlib.import_module('tensorflow.keras')
from keras.models import load_model
import matplotlib.pyplot as plt
import time
from PIL import Image

# ------------------------------------------------------------------------------------------------------------------
# Funciones
# ------------------------------------------------------------------------------------------------------------------

def decoderDL(vecdeser, name_trained_decoder_model, output_image_path):
    """
    Define una función llamada encoderDL que se encarga de comprimir una imagen RGB en un vector de datos
    :param folder_path: directorio de la imagen
    :param trained_encoder_model: modelo del codificador entrenado
    :return:
    """
    # # Carga del modelo con Tensorflow
    # trained_decoder_model = load_model(name_trained_decoder_model)
    # trained_decoder_model.summary()
    # Carga del modelo con Tensorflow Lite
    trained_decoder_model = load_model(name_trained_decoder_model)
    trained_decoder_model.summary()
    # Hacer la inferencia con el modelo del decoder
    inicio_decoder = time.time()
    reconstructed_image = trained_decoder_model.predict(vecdeser)
    fin_decoder = time.time()
    tiempo_inferencia_decoder = fin_decoder - inicio_decoder
    print("Tiempo de inferencia para el decoder:", tiempo_inferencia_decoder, "segundos")
    # Post-procesamiento de la imagen reconstruida
    # Escalar a [0, 255] y convertir a uint8
    reconstructed_image = (reconstructed_image * 255).astype(np.uint8)
    # Convertir el tensor a una imagen PIL, eliminando la dimensión del batch (1, 64, 64, 3)
    print('print(reconstructed_image[0]: ', reconstructed_image[0])
    reconstructed_image_pil = Image.fromarray(reconstructed_image[0])
    # Guardar la imagen reconstruida
    reconstructed_image_pil.save(output_image_path)
    print(f"Imagen reconstruida guardada en: {output_image_path}")

    return reconstructed_image_pil


def plotImage(reconstructed_image_name):
    """
    Este código define una función llamada sendVector que se encarga de enviar un vector de datos
    a través de un socket UDP.
    :param host: dirección IP o el nombre del dominio del servidor con el que se desea establecer una comunicación
    :param port: canal específico por el cual el socket se comunica con el servidor
    :param vector: contiene los datos de imagen en una representación de pocas características
    :param fragmentSize: divide al vector en fragmentos para enviarse al servidor mediante un bucle
    :return: None
    """
    # Mostrar la imagen
    plt.imshow(reconstructed_image_name)
    # Ocultar los ejes
    plt.axis('off')
    # Mostrar el plot
    plt.show()

    return None


def start_server(host='192.168.0.10', port=23):
    # Crear el socket
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
            vecdeser = pickle.loads(data)

        finally:
            return vecdeser
            client_socket.close()

if __name__ == "__main__":

    # ------------------------------------------------------------------------------------------------------------------
    # Variables y configuración
    # ------------------------------------------------------------------------------------------------------------------

    # Pedir al usuario que ingrese un número entero
    dim = int(input("Ingrese las dimensión: "))
    dim_s = str(dim)

    # Directorio del modelo
    decoder_model = r'decoder_fire_model_' + dim_s + 'x' + dim_s +'_paper.h5'
    output_img_path = 'reconstructed_image.jpg'

    # ------------------------------------------------------------------------------------------------------------------
    # Llamadas a las funciones
    # ------------------------------------------------------------------------------------------------------------------

    vecdeser = start_server()
    rec_image = decoderDL(vecdeser, decoder_model, output_img_path)
    plotImage(rec_image)
