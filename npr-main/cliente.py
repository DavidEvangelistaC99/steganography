"""
Imágenes codificadas a vectores usando Deep Learning
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
from keras.preprocessing.image import load_img, img_to_array
import importlib
keras = importlib.import_module('tensorflow.keras')
from keras.models import load_model
import os
import matplotlib.pyplot as plt
import sys
import time

# ------------------------------------------------------------------------------------------------------------------
# Funciones
# ------------------------------------------------------------------------------------------------------------------

def encoderDL(folder_path, name_trained_encoder_model,dim):
    """
    Define una función llamada encoderDL que se encarga de comprimir una imagen RGB en un vector de datos
    :param folder_path: directorio de la imagen
    :param trained_encoder_model: modelo del codificador entrenado
    :return:
    """

    test_images_orig = []

    while True:
        # Lista de archivos en la carpeta
        file_list = os.listdir(folder_path)
        file_list_sorted = sorted(file_list)

        if file_list[0]:
            # Imagen seleccionada
            img_path = os.path.join(folder_path, file_list_sorted[10])
            print('Nombre de la imagen: ', img_path)
            peso_bytes_imagen = os.path.getsize(img_path)
            print(f"El peso de la imagen antes de ser redimensionada es:", peso_bytes_imagen, 'bytes')
            img = load_img(img_path, target_size=(dim,dim))
            img_array = img_to_array(img) / 255.0
            test_images_orig.append(img_array)
            # Cargando el modelo entrenado del encoder
            trained_encoder_model = load_model(name_trained_encoder_model, compile=False)
            test_images = np.array(test_images_orig)
            # Hacer la inferencia con el modelo del encoder para obtener los vectores de salida del codificador
            inicio_encoder = time.time()
            encoded_vector = trained_encoder_model.predict(test_images)
            fin_encoder = time.time()
            tiempo_inferencia_encoder = fin_encoder - inicio_encoder
            print("Tiempo de inferencia para codificar:", tiempo_inferencia_encoder, "segundos")

            return encoded_vector
        else:
            print('¡Capture una imagen RGB para comenzar con la compresión y su posterior transmisión UHF!')


def send_data(data, host='192.168.0.10', port=23):
    # Crear el socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        # Registrar tiempo de inicio
        start_time = time.time()
        # Enviar los datos
        client_socket.sendall(data)
        # Registrar tiempo de termino
        end_time = time.time()
        # Tiempo de envio
        elapsed_time = end_time - start_time
        print('Datos enviados')
        print(f'Tiempo de envío: {elapsed_time:.4f} segundos')

    finally:
        client_socket.close()


if __name__ == "__main__":

    # ------------------------------------------------------------------------------------------------------------------
    # Variables y configuración
    # ------------------------------------------------------------------------------------------------------------------

    # Ingreso de la dimensión
    dim = int(input('Ingrese la dimensión: '))
    dim_s = str(dim)

    # Directorio de la imagen
    folder_path = r'' + dim_s + 'x' + dim_s
    # Modelo entrenado
    model = r'encoder_fire_model_' + dim_s + 'x' + dim_s + '_paper.h5'

    # ------------------------------------------------------------------------------------------------------------------
    # Llamadas a las funciones
    # ------------------------------------------------------------------------------------------------------------------

    tensor = encoderDL(folder_path, model,dim)
    vecser = pickle.dumps(tensor)
    print('VecSer:\n', vecser)
    print(len(vecser))
    send_data(vecser)
