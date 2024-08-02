import cv2
import numpy as np
import math

from PIL import Image

#8 reference bits
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
	for bit in caracter_terminacion:
		lista.append(bit)
	return lista

def canny_route(image_input):
    img = cv2.imread(image_input)
    bordesCanny = cv2.Canny(img,100,200)
    cv2.imwrite("canny.png",bordesCanny)
    canny = cv2.imread("canny.png")
    canny = canny.astype(np.float32)
    cv2.imwrite("canny32bits.png", canny, [cv2.IMWRITE_PNG_COMPRESSION,9])
    return "canny32bits.png"

def stgn_in(original_route,data):
    print("Hiding message...")

    #Canny Filter
    canny = canny_route(original_route)

    #Load images
    image = Image.open(original_route)
    canny_ = Image.open(canny)

    #RGB values for pixels
    pixels = image.load()
    canny_pixels = canny_.load()

    #Number of pixels (width and height)
    size = image.size
    width = size[0]
    height = size[1]

    #Binary message of data
    string = obtener_lista_de_bits(data)
    length = len(string)

    count = 0

    for x in range(height):
        for y in range(width):
            #RGB List of pixel (R,G,B)
            pixel = pixels[y,x]
            canny_pixel = canny_pixels[y,x]

            R_c = canny_pixel[0]
            G_c = canny_pixel[1]
            B_c = canny_pixel[2]

            R = pixel[0]
            G = pixel[1]
            B = pixel[2]

            if(R_c == 255 and G_c == 255 and B_c == 255):
                
                if count < length:
                    if(count < length):
                        new_R = modificar_color(R,string[count])
                        count += 1
                    else:
                        new_R = R
                    if(count < length):
                        new_G = modificar_color(G,string[count])
                        count += 1
                    else:
                        new_G = G
                    if(count < length):
                        new_B = modificar_color(B,string[count])
                        count += 1
                    else:
                        new_B = B

                    pixels[y,x] = (new_R,new_G,new_B)
                else:
                    break
    
    print("Hided Message")
    image.save("outCanny.png")
	