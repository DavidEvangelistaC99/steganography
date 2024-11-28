"""
Escenario de pruebas 1
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías de esteganografía desarrolladas
# ------------------------------------------------------------------------------------------------------------------

'''
import steganographyPaper as stgnP
import steganographyStats as stgnS
import statistics as stats
import steganography1LSB as stgn1LSB
import steganography2LSB as stgn2LSB
import steganographyCanny as stgnC
import comparisonCanny as comC
import parameters as pmt
'''

# ------------------------------------------------------------------------------------------------------------------
# Variables y Funciones
# ------------------------------------------------------------------------------------------------------------------

# Imagen original
image_route_in = "lenna_gris.png"
# Imagen esteganográfica
image_route_out = "out.png"
# Imagen recuperada
image_bit_out = "bitOutLenna.png"

# Primer mensaje de prueba
message_01 = "hi"
# Mensaje a enviar para las pruebas de transmisión
# El mensaje tiene 38 caracteres, equivalente a 38x8 = 304 bits
message_02 = "Temp: 25.06°C, Hum: 53%, Pre: 0.98 atm"
# Mensaje de prueba para el umbral
# El mensaje tiene 562 caracteres, equivalente a 562x8 = 4496 bits
message_03 = "Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido. También es una composición de caracteres imprimibles (con grafema) generados por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original. En otras palabras, un texto es un entramado de signos con una intención comunicativa que adquiere sentido en determinado contexto.Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido."

# Umbral
T = 15

# Umbral variable
Tmin = 10
Tmax = 20

# Semilla
seed = 0

# Algoritmo Canny
canny_out = "outCanny.png"
canny_out_1 = "canny.png"
canny_out_2 = "canny32Bits.png"
canny_comp = "comparisonCanny.png"

'''
#// Steganography Paper
# Parameters SNR, SSIM
stgnP.stgn_in(image_route_in,image_route_out,message_02,T)
print(stgnP.stgn_out(image_route_out,image_bit_out,T))

psnr1 = pmt.calculate_psnr("Lenna_512x512_In.bmp","Lenna_512x512_Out.bmp")
print(f"PSNR Stego: {psnr1} dB")
'''

'''
psnr2 = pmt.calculate_psnr(image_route_in,image_bit_out)
print(f"PSNR Bit Out: {psnr2} dB")
ssim1 = pmt.calculate_ssim("Lenna_512x512_In.bmp","Lenna_512x512_Out.bmp")
print(f"SSIM Stego: {ssim1}")
'''

'''
ssim2 = pmt.calculate_ssim(image_route_in,image_bit_out)
print(f"SSIM Bit Out: {ssim2}")

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