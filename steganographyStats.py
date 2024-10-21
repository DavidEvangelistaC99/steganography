"""
Algoritmo principal de esteganografía ([DavidE3] para imágenes RGB)
Contrarresto de la anomalía en la distribución de diferencias entre píxeles adyacentes
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías
# ------------------------------------------------------------------------------------------------------------------


import numpy as np
from PIL import Image
import random

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

#Creation of Pixel Matrix
def image_matrix(image_route):
    #Objeto Image
    image = Image.open(image_route)
    
    #Image Dimensions
    x_lim = image.size[0]
    y_lim = image.size[1]

    #Pixels load
    pixels = image.load()
    #  __ __ __ x
    # |
    # |
    # |
    # y
    
    I = np.empty((y_lim,x_lim),dtype = object)

    #Horizontal path
    for y in range(y_lim):
        for x in range(x_lim):
            pixel = pixels[x,y]
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]

            #512x512 Matrix (I[x][y]=[R,G,B])
            I[y,x] = [R, G, B]

    return I

def pixelChange(image_route,image_out,matrix):
    #Objeto Image
    image = Image.open(image_route)

    x_lim = image.size[0]
    y_lim = image.size[1]

    pixels = image.load()
    #pixels[x,y]
    #  __ __ __ x
    # |
    # |
    # |
    # y

    for y in range(y_lim):
        for x in range(x_lim):
            pixels[x,y] = tuple(matrix[y,x])
    
    image.save(image_out)

#What if R,G or B is 255?
#Steganography Application
def stgn_in(image_route,image_out,message,Tmin,Tmax,s):
    #Random seed
    random.seed(s)

    #Creation of Pixel Matrix
    I = image_matrix(image_route) #---> I == image_route

    #Get binary code of message
    binary = getBinary(message)
    length = len(binary)
    count = 0

    #Image Dimensions
    x_lim = len(I[0,:])
    if(len(I[0,:])%2 != 0):
        x_lim = x_lim - 1
    
    y_lim = len(I[:,0])

    #Horizontal path
    #for using len(): limited to length of array
    for y in range(y_lim):                
        for x in range(0,x_lim,2):
            
            #Random number
            T = random.randint(Tmin,Tmax)

            if(count < length):
                #Pixels (a,b) consecutive pair
                a = I[y,x]
                b = I[y,x+1]

                #Difference of pixels (Threshold verification for RGB)
                for i in range(3):
                    a_i = a[i]
                    b_i = b[i]

                    dif = abs(a_i - b_i)

                    #Threshold verification for RGB
                    if((dif >= T) and (count < length)):
                        
                        if(a[i]%2 == binary[count]):
                            a_i = a_i
                            count = count + 1
                        else:
                            if(a_i > b_i):
                                a_i = a_i + 1
                                count = count + 1
                            else:
                                if(a_i < b_i):
                                    a_i = a_i - 1
                                    count = count + 1
                            
                    I[y,x][i] = a_i 
                    
                    if(count>=length):
                        break

            else:
                break
    
    pixelChange(image_route,image_out,I)
    return I

def stgn_out(image_route,Tmin,Tmax,s):
    #Random seed
    random.seed(s)

    #Creation of Pixel Matrix
    I = image_matrix(image_route)
    
    #Image Dimensions
    x_lim = len(I[0,:])
    if(len(I[0,:])%2 != 0):
        x_lim = x_lim - 1

    y_lim = len(I[:,0])

    #Message array
    message = []

    #8 bits array
    bit = np.zeros(8)
    count = np.zeros(1)

    for y in range(y_lim):
        for x in range(0,x_lim,2):
            #Random number
            T = random.randint(Tmin,Tmax)

            #Pixels (a,b) consecutive pair
            a = I[y,x]
            b = I[y,x+1]

            #Difference of pixels (Threshold verification for RGB)
            for i in range(3):
                dif = abs(a[i] - b[i])

                if(dif >= T):
                    count[0] = a[i]%2
                    message = np.concatenate((message,count))
                    bit = np.roll(bit,1)
                    bit[0] = count[0]

                    if(len(message)%8 == 0 and decimalCode(bit[-8:]) == 255):
                        return getMessage(message)
