"""
Algoritmo principal de esteganografía utilizando el filtro de Canny
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías
# ------------------------------------------------------------------------------------------------------------------

import cv2
import numpy as np
from PIL import Image

# ------------------------------------------------------------------------------------------------------------------
# Variable y Funciones
# ------------------------------------------------------------------------------------------------------------------

#8 bits de terminación
caracter_terminacion = [1, 1, 1, 1, 1, 1, 1, 1]

def obtener_representacion_ascii(caracter):
    return ord(caracter)

def obtener_representacion_binaria(numero):
    return bin(numero)[2:].zfill(8)

def cambiar_ultimo_bit(byte, nuevo_bit):
    return byte[:-1] + str(nuevo_bit)

def binario_a_decimal(binario):
    return int(binario, 2)

def modificar_color(color_original, bit):
    color_binario = obtener_representacion_binaria(color_original)
    color_modificado = cambiar_ultimo_bit(color_binario, bit)
    return binario_a_decimal(color_modificado)

def obtener_lista_de_bits(texto):
    lista = []
    for letra in texto:
        representacion_ascii = obtener_representacion_ascii(letra)
        representacion_binaria = obtener_representacion_binaria(representacion_ascii)
        for bit in representacion_binaria:
            lista.append(bit)
    #Añadir los bits de terminación
    lista.extend(caracter_terminacion)
    return lista

def bits_a_texto(bits):
    texto = ''
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i + 8]
        if len(byte_bits) < 8:
            break
        byte = binario_a_decimal(''.join(byte_bits))
        if byte == 0:
            break
        texto += chr(byte)
    return texto

#Función para obtener la imagen Canny en formato .png
def canny_route(image_input, image_out_1, image_out_2):
    #image_out_1 -> canny.png
    #image_out_2 -> canny32Bits.png

    img = cv2.imread(image_input)

    #Aplicar Canny Edge
    bordesCanny = cv2.Canny(img, 100, 150)
    cv2.imwrite(image_out_1, bordesCanny)
    canny = cv2.imread(image_out_1)
    canny = canny.astype(np.float32)
    cv2.imwrite(image_out_2, canny, [cv2.IMWRITE_PNG_COMPRESSION, 9])


def stgn_in(original_route, canny_out, canny_out_1, canny_out_2, data):
    #Aplicar filtro Canny
    canny_route(original_route, canny_out_1, canny_out_2)

    #Cargar imágenes
    image = Image.open(original_route)
    canny = Image.open(canny_out_2)

    pixels = image.load()
    canny_pixels = canny.load()

    #Tamaño de la imagen (ancho y alto)
    width, height = image.size

    #Mensaje binario del dato
    string = obtener_lista_de_bits(data)
    length = len(string)

    count = 0

    for y in range(height):  #Recorrer filas (coordenada Y)
        for x in range(width):  #Recorrer columnas (coordenada X)
            #Lista RGB del píxel
            pixel = pixels[x, y]
            canny_pixel = canny_pixels[x, y]

            R_c = canny_pixel[0]
            G_c = canny_pixel[1]
            B_c = canny_pixel[2]

            R = pixel[0]
            G = pixel[1]
            B = pixel[2]

            if R_c == 255 and G_c == 255 and B_c == 255:  # Solo modificar píxeles blancos de Canny
                if count < length:
                    new_R = modificar_color(R, string[count])
                    count += 1
                else:
                    new_R = R
                if count < length:
                    new_G = modificar_color(G, string[count])
                    count += 1
                else:
                    new_G = G
                if count < length:
                    new_B = modificar_color(B, string[count])
                    count += 1
                else:
                    new_B = B

                pixels[x, y] = (new_R, new_G, new_B)

    print(data)
    image.save(canny_out)

def stgn_out(image_out,canny_out_2):
    #Leer la imagen esteganográfica
    image = Image.open(image_out)
    pixels = image.load()

    canny_image = Image.open(canny_out_2)
    canny_pixels = canny_image.load()

    #Tamaño de la imagen
    width, height = image.size

    #Extraer bits de la imagen
    bits = []
    for y in range(height):
        for x in range(width):
            #Píxeles de la imagen original y la imagen Canny
            pixel = pixels[x, y]
            canny_pixel = canny_pixels[x, y]

            R_c, G_c, B_c = canny_pixel
            R, G, B = pixel

            if R_c == 255 and G_c == 255 and B_c == 255:  # Solo píxeles blancos
                #Obtener el último bit de cada componente de color
                bits.append(bin(R)[-1])
                bits.append(bin(G)[-1])
                bits.append(bin(B)[-1])

                #Verificar si se ha encontrado la secuencia de terminación
                if len(bits) >= len(caracter_terminacion):
                    if bits[-len(caracter_terminacion):] == [str(bit) for bit in caracter_terminacion]:
                        bits = bits[:-len(caracter_terminacion)]
                        break
        else:
            continue
        break

    texto_oculto = bits_a_texto(bits)

    return texto_oculto
