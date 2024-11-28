"""
Funciones de compresión
INICTEL-2024
@david_evangelista
""" 

# ------------------------------------------------------------------------------------------------------------------
# Librerías
# ------------------------------------------------------------------------------------------------------------------

import numpy as np
import cv2
import zigzag as zg

# ------------------------------------------------------------------------------------------------------------------
# Variables y Funciones
# ------------------------------------------------------------------------------------------------------------------

QUANTIZATION_MAT = np.array([[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56 ],[14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],[49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]])

def schemaSubsampling (bloque, a, b):

    if a == 4 and b == 4:
        bloque = bloque
    else:
        if a == 2:
            for i in range(0, bloque.shape[1], 2):
                if i < bloque.shape[1]:
                    bloque[0, i:i+2] = bloque[0, i]
                if i + 1 < bloque.shape[1]:
                    bloque[1, i:i+2] = bloque[1, i]

            if b == 0:
                bloque[1] = bloque[0]

    return bloque

def subsamplingChroma(channel, j, a, b):
    # Dimensiones de la imagen
    h, w = channel.shape
    # Dimensiones del bloque de submuestreo
    columns = j
    rows = 2

    subSampling = np.zeros_like(channel)
    bloque = []
    
    # Recorre la matriz por bloques
    for y in range(0, h, rows):  # Recorrido de filas primero
        for x in range(0, w, columns):  # Recorrido de columnas
            if y + rows <= h and x + columns <= w:
                bloque = channel[y:y + rows, x:x + columns]
                bloqueNew = schemaSubsampling(bloque, a, b)
                subSampling[y:y + rows, x:x + columns] = bloqueNew
    if j == 4 and a == 2 and b == 0:
        subSampling = subSampling[::2, ::2]
    
    return subSampling

def dct(imageMatrix):

    imageMatrix_ = np.float32(imageMatrix)

    # Dimensiones de la imagen
    h, w = imageMatrix_.shape
    # Dimensiones del bloque de submuestreo
    columns = 8
    rows = 8
    
    dctMatrix = np.zeros_like(imageMatrix_)
    bloque = []
    
    # Recorre la matriz por bloques
    for y in range(0, h, rows):  # Recorrido de filas primero
        for x in range(0, w, columns):  # Recorrido de columnas
            if y + rows <= h and x + columns <= w:
                bloque = imageMatrix_[y:y + rows, x:x + columns]
                dct_ = cv2.dct(bloque)
                bloqueNew = np.divide(dct_, QUANTIZATION_MAT).astype(int)
                dctMatrix[y:y + rows, x:x + columns] = bloqueNew

    return dctMatrix

def createText(imageMatrix, routeTxt):
    # Dimensiones de la imagen
    h, w = imageMatrix.shape
    # Dimensiones del bloque de submuestreo
    columns = 8
    rows = 8

    paddedImage = np.zeros_like(imageMatrix)
    bloque = []
    
    # Recorre la matriz por bloques
    for y in range(0, h, rows):  # Recorrido de filas primero
        for x in range(0, w, columns):  # Recorrido de columnas
            if y + rows <= h and x + columns <= w:
                bloque = imageMatrix[y:y + rows, x:x + columns]
                # -- #
                reordered = zg.zigzag(bloque)
                reshaped = np.reshape(reordered, (columns, rows))
                # -- #
                paddedImage[y:y + rows, x:x + columns] = reshaped
    
    arranged = paddedImage.flatten()

    # Now RLE encoded data is written to a text file (You can check no of bytes in text file is very less than no of bytes in the image
    # THIS IS COMPRESSION WE WANTED, NOTE THAT ITS JUST COMPRESSION DUE TO RLE, YOU CAN COMPRESS IT FURTHER USING HUFFMAN CODES OR MAY BE 
    # REDUCING MORE FREQUENCY COEFFICIENTS TO ZERO)

    bitstream = lengthEncoding(arranged)

    # Two terms are assigned for size as well, semicolon denotes end of image to reciever
    bitstream = str(paddedImage.shape[0]) + " " + str(paddedImage.shape[1]) + " " + bitstream + ";"

    # Written to image.txt
    file1 = open(routeTxt, "w")
    file1.write(bitstream)
    file1.close()

def lengthEncoding(image):
    i = 0
    skip = 0
    stream = []    
    bitstream = ""
    image = image.astype(int)
    while i < image.shape[0]:
        if image[i] != 0:            
            stream.append((image[i],skip))
            bitstream = bitstream + str(image[i]) + " " + str(skip) + " "
            skip = 0
        else:
            skip = skip + 1
        i = i + 1

    return bitstream

def getStegoMatrix(route_image):
    
    # defining block size
    block_size = 8

    # Reading image.txt to decode it as image
    with open(route_image, 'r') as image_file:
        image = image_file.read()

    # spplits into tokens seperated by space characters
    details = image.split()

    # just python-crap to get integer from tokens : h and w are height and width of image (first two items)
    h = int(''.join(filter(str.isdigit, details[0])))
    w = int(''.join(filter(str.isdigit, details[1])))

    # declare an array of zeros (It helps to reconstruct bigger array on which IDCT and all has to be applied)
    array = np.zeros(h*w).astype(int)

    # some loop var initialisation
    k = 0
    i = 2
    x = 0
    j = 0

    # This loop gives us reconstructed array of size of image

    while k < array.shape[0]:
    # Oh! image has ended
        if(details[i] == ';'):
            break
    # This is imp! note that to get negative numbers in array check for - sign in string
        if "-" not in details[i]:
            array[k] = int(''.join(filter(str.isdigit, details[i])))        
        else:
            array[k] = -1*int(''.join(filter(str.isdigit, details[i])))        

        if(i+3 < len(details)):
            j = int(''.join(filter(str.isdigit, details[i+3])))

        if j == 0:
            k = k + 1
        else:                
            k = k + j + 1        

        i = i + 2

    array = np.reshape(array,(h,w))

    # loop for constructing intensity matrix form frequency matrix (IDCT and all)
    i = 0
    j = 0
    k = 0

    # initialisation of compressed image
    padded_img = np.zeros((h,w))

    while i < h:
        j = 0
        while j < w:        
            temp_stream = array[i:i+8,j:j+8]                
            block = zg.inverse_zigzag(temp_stream.flatten(), int(block_size),int(block_size))               
            padded_img[i:i+8,j:j+8] = block     
            j = j + 8        
        i = i + 8

    return padded_img

def idct(imageMatrix):
    # Dimensiones de la imagen
    h, w = imageMatrix.shape
    # Dimensiones del bloque de submuestreo
    columns = 8
    rows = 8

    idctMatrix = np.zeros_like(imageMatrix)
    bloque = []
    
    # Recorre la matriz por bloques
    for y in range(0, h, rows):  # Recorrido de filas primero
        for x in range(0, w, columns):  # Recorrido de columnas
            if y + rows <= h and x + columns <= w:
                bloque = imageMatrix[y:y + rows, x:x + columns]
                idct_ = np.multiply(bloque, QUANTIZATION_MAT)
                bloqueNew = cv2.idct(np.float32(idct_))
                idctMatrix[y:y + rows, x:x + columns] = bloqueNew

    return idctMatrix