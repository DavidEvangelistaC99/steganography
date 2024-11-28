"""
Funciones de revisión estadística
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías
# ------------------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import steganographyPaper as stgn

# ------------------------------------------------------------------------------------------------------------------
# Funciones
# ------------------------------------------------------------------------------------------------------------------

# Histograma que muestra la cantidad de píxeles de la imagen con determinado valor en cada banda.
def histogramRGB(image_route):
    #Creation of Pixel Matrix
    I = stgn.image_matrix(image_route)

    #Image Dimensions
    x_lim = len(I[0,:])
    y_lim = len(I[:,0])

    #Histogram array
    hist = np.zeros((3,256))

    #Graphic axis X
    N = np.zeros(256)
    for i in range(256):
        N[i] = i

    for y in range(y_lim):
        for x in range(x_lim):
            
            #Pixels
            pixel = I[y,x]

            for i in range(3):
                RGB = pixel[i]
                hist[i,RGB] = hist[i,RGB] + 1

    plt.plot(N,hist[0,:],'red')
    plt.plot(N,hist[1,:],'green')
    plt.plot(N,hist[2,:],'blue')
    plt.grid()
    plt.show()

# Histograma de las diferencias de los valores de los píxeles consecutivos de una imagen que cumplen determinado umbral
# "n" representa el numero de diferencias mostrado en la gráfica
def histogramDifference(image_route, n):
    #Creation of Pixel Matrix
    I = stgn.image_matrix(image_route)

    #Difference histogram
    hist = np.zeros(2*n+1)
    N = np.zeros(2*n+1)

    #Image Dimensions
    x_lim = len(I[0,:])
    if(len(I[0,:])%2 != 0):
        x_lim = x_lim - 1
    
    y_lim = len(I[:,0])

    for y in range(y_lim):
        for x in range(0,x_lim,2):

            #Pixels (a,b) consecutive pair
            a = I[y,x]
            b = I[y,x+1]

            #Difference of pixels (Threshold verification for RGB)
            for i in range(3):
                a_i = a[i]
                b_i = b[i]
                dif = a_i - b_i

                if(abs(dif) < n):
                    hist[dif + n] = hist[dif + n] + 1

    for i in range(2*n-1):
        N[i] = i - n

    plt.bar(N,hist)
    plt.show()
