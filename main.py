"""
Escenario de pruebas
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías de esteganografía desarrolladas
# ------------------------------------------------------------------------------------------------------------------

import steganographyPaper as stgnP
import steganographyStats as stgnS
import statistics as stats
import steganography1LSB as stgn1LSB
import steganography2LSB as stgn2LSB
import steganographyCanny as stgnC
import comparisonCanny as comC

# ------------------------------------------------------------------------------------------------------------------
# Variables y Funciones
# ------------------------------------------------------------------------------------------------------------------

image_route_in = "Lenna.png"
image_route_out = "outLenna.png"

# Primer mensaje de prueba
message_01 = "hi"

# Mensaje de prueba para el umbral
message_02 = "Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original."

# Mensaje a enviar para las pruebas de transmisión
message_03 = "Temp: 25.06°C, Hum: 53%, Pre: 0.98 atm"

# Umbral
T = 15

# Umbral variable
Tmin = 10
Tmax = 20

# Semilla
seed = 0

# Algortimo Canny
canny_out = "outCanny.png"
canny_out_1 = "canny.png"
canny_out_2 = "canny32Bits.png"
canny_comp = "comparisonCanny.png"

'''
#// Steganography Paper
stgnP.stgn_in(image_route_in,image_route_out,message_03,T)
print(stgnP.stgn_out(image_route_out,T))

# Histogramas iniciales
stats.histogramRGB(image_route_in)
stats.histogramDifference(image_route_in,20)

# Histogramas finales
stats.histogramRGB(image_route_out)
stats.histogramDifference(image_route_out,20)
'''

'''
#// Steganography Statistics
stgnS.stgn_in(image_route_in,image_route_out,message_03,Tmin,Tmax,seed)
print(stgnS.stgn_out(image_route_out,Tmin,Tmax,seed))

# Histogramas iniciales
stats.histogramRGB(image_route_in)
stats.histogramDifference(image_route_in,20)

# Histogramas finales
stats.histogramRGB(image_route_out)
stats.histogramDifference(image_route_out,20)
'''

'''
#// Steganography 1LSB
stgn1LSB.stgn_in(image_route_in,image_route_out,message_03)
print(stgn1LSB.stgn_out(image_route_out))
'''

'''
#// Steganography 2LSB
stgn2LSB.stgn_in(image_route_in,image_route_out,message_02)
print(stgn2LSB.stgn_out(image_route_out))
'''

'''
#// Steganography Canny
stgnC.stgn_in(image_route_in,canny_out,canny_out_1,canny_out_2,message_02)
print(stgnC.stgn_out(canny_out,canny_out_2))

#//Find Difference
comC.find_difference(image_route_in,canny_out,canny_comp)
'''