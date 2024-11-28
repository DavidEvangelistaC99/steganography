"""
Escenario de pruebas de compresión
(Cliente)
INICTEL-2024
@david_evangelista
""" 

# ------------------------------------------------------------------------------------------------------------------
# Librerías de esteganografía desarrolladas
# ------------------------------------------------------------------------------------------------------------------

import cv2
import numpy as np
import process
from scipy.ndimage import zoom
import steganographyPaper as stgnP
import client

# ------------------------------------------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------------------------------------------

image_route = "imagenCultivo.jpeg"

# Imagen en BGR
img_bgr = cv2.imread(image_route)

# Convertir imagen en formato BGR a RGB
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Convertir imagen en formato RGB a Y, Cr, Cb
img_ycrcb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2YCrCb)

# Separate channels
Y, Cr, Cb = cv2.split(img_ycrcb)

chromaR = process.subsamplingChroma(Cr, 4, 2, 0)
chromaB = process.subsamplingChroma(Cb, 4, 2, 0)

DCTQR = process.dct(chromaR)
DCTQB = process.dct(chromaB)

# Esteganografía en frecuencia
# Imagen esteganográfica
image_route_out = "stegoImageDCTQ.bmp"
# Mensaje a enviar para las pruebas de transmisión
# El mensaje tiene 38 caracteres, equivalente a 38x8 = 304 bits
message = "Temp 25.06°C, Hum 53%"
# Umbral
T = 10

# Imagen DCTQ Esteganográfica
DCTQR_ = stgnP.stgn_in(DCTQR, image_route_out, message, T)

# Creación de los archivos .txt
routeTxtR = "Lenna_Restored_R.txt"
paddedImage = process.createText(DCTQR_, routeTxtR)

routeTxtB = "Lenna_Restored_B.txt"
paddedImage = process.createText(DCTQB, routeTxtB)

### TRANSMISIÓN ###
# En esta parte se envían las siguientes variables:
# 1. DCTQR_ (txt)
# 2. DCTQB  (txt)
# 3. Y      (list)

# Llamada a las funciones de transmisión (Cliente)
client_posible.sendData(routeTxtR, routeTxtB, Y)

#### RECEPCIÓN ####
