import steganographyPaper as stgnP
import steganographyBasic as stgnB
import steganographyStats as stgnS
import steganography2LSB as stgn2LSB
import steganographyCanny as stgnC
import comparisonCanny as comC
import statistics as stats

image_route_in = "Lenna.png"
image_route_out_stats = "outStats.png"
message_01 = "hi"
message_02 = "Temp: 25.06°C, Hum: 53%, Pre: 0.98 atm"
message_03 = "Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto."
T = 10
Tmin = 10
Tmax = 20
seed = 0
n = 30

'''
stgnP.stgn_in(image_route_in,message_01,T)
print(stgnP.stgn_out("outP.png",T))

stgnB.stgn_in(image_route_in,message_01)
print(stgnB.stgn_out("outB.png"))

stgn2LSB.stgn_in(image_route_in,message_01)
print(stgn2LSB.stgn_out("out2LSB.png"))
'''

stgnC.stgn_in(image_route_in,message_03)
#Find Difference
comC.find_difference("Lenna.png","outCanny.png")