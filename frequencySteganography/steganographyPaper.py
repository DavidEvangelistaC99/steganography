"""
Algoritmo principal de esteganografía ([DavidE3] para imágenes RGB)
INICTEL-2024
@david_evangelista
Obervación: Se realizaron algunos cambios con respecto al original debido a la forma de la matriz comprimida resultante
	    (Este programa no es igual a la desarrollada en la Esteganografía espacial)
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías
# ------------------------------------------------------------------------------------------------------------------

import numpy as np
import cv2

# ------------------------------------------------------------------------------------------------------------------
# Variable y Funciones
# ------------------------------------------------------------------------------------------------------------------

#8 reference bits
referBits = np.ones(8)

#ASCII Code Development
def asciiCode(character):
	return ord(character)

#Binary Code Development (every 8 bits)
def binaryCode(number):
    decimal = int(bin(number)[2:].zfill(8))
    binary = list(range(8))
    for i in range(8):
        binary[7-i] = decimal%10
        decimal = decimal//10

    return binary

#Convert binary to decimal number
def decimalCode(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal = decimal + binary[7-i]*(2**i)
    
    return decimal

#Get binary representation of message
def getBinary(message):
    bits = []
    for i in message:
        ascii_ = asciiCode(i)
        binary_ = binaryCode(ascii_)
        bits = bits + binary_
    #bits = bits + referBits
    bits = np.concatenate((bits,referBits))

    return bits

def getMessage(array):
    #Create message
    message = ""
    length = len(array)
    length = int(length/8)

    for i in range(length-1):
        letterBin = array[i*8:i*8+8]
        letterDec = decimalCode(letterBin)
        letter = chr(int(letterDec))
        message = message + letter

    return message

#What if R,G or B is 255?
#Steganography Application
def stgn_in(matrix, image_out, message, T):
    #Creation of Pixel Matrix
    I = matrix

    #Get binary code of message
    binary = getBinary(message)
    length = len(binary)
    count = 0

    #Image Dimensions
    h, w = I.shape

    #Horizontal path
    #for using len(): limited to length of array
    for y in range(h):                
        for x in range(0, w, 2):
            
            if(count < length):
                #Pixels (a,b) consecutive pair
                a = I[y, x]
                b = I[y, x + 1]

                #Difference of pixels (Threshold verification for RGB)
                dif = abs(a - b)

                #Threshold verification for RGB
                if((dif >= T) and (count < length)):
                        
                    if(a % 2 == binary[count]):
                        a = a
                        count = count + 1
                    else:
                        if(a > b):
                            a = a + 1
                            count = count + 1
                        else:
                            if(a < b):
                                a = a - 1
                                count = count + 1
                            
                    I[y,x] = a 
                    
                    if(count>=length):
                        break

            else:
                break
    
    # I_ = np.clip(I, 0, 255)
    # cv2.imwrite(image_out, np.uint8(I_))

    return I

def stgn_out(I,T):
    #Pixel Matrix
    I = np.float32(I)

    #Image Dimensions
    h, w = I.shape

    #Message array
    message = []

    #8 bits array
    bit = np.zeros(8)
    count = np.zeros(1)

    for y in range(h):
        for x in range(0, w, 2):

            #Pixels (a,b) consecutive pair
            a = I[y, x]
            b = I[y, x + 1]

            #Difference of pixels (Threshold verification for RGB)
            #Cambio por range(1)
            dif = abs(a - b)

            if(dif >= T):
                count[0] = a % 2
                message = np.concatenate((message,count))
                bit = np.roll(bit,1)
                bit[0] = count[0]

                if(len(message) % 8 == 0 and decimalCode(bit[-8:]) == 255):
                    return getMessage(message)
