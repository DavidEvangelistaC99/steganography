"""
Escenario de pruebas de compresión
(Servidor)
INICTEL-2024
@david_evangelista
""" 

# ------------------------------------------------------------------------------------------------------------------
# Librerías de esteganografía desarrolladas
# ------------------------------------------------------------------------------------------------------------------

import cv2
import numpy as np
import process
import parameters as pmt
from scipy.ndimage import zoom
import server
import steganographyPaper as stgnP

# ------------------------------------------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------------------------------------------

#### RECEPCIÓN ####

file = "imagenCultivo.bmp"
T = 10

routeTxtR = 'Lenna_RestoredR.txt'
routeTxtB = 'Lenna_RestoredB.txt'
Y = server.receiveData(routeTxtR, routeTxtB)

# Recuperación de la matriz esteganográfica
matrixRecoveredR = process.getStegoMatrix(routeTxtR)
matrixRecoveredB = process.getStegoMatrix(routeTxtB)

# Recuperación de Cr Submuestreada Recuperada
crRecovered = process.idct(matrixRecoveredR)
crRecovered = np.uint8(crRecovered)

cbRecovered = process.idct(matrixRecoveredB)
cbRecovered = np.uint8(cbRecovered)

# Aplicación del Algortimo Bicúbico (Aumento de dimensión)
crRecovered_ = zoom(crRecovered, 2, order = 3)
cbRecovered_ = zoom(cbRecovered, 2, order = 3)
yRecovered_ = Y

# Reformar la matriz
print(crRecovered_.shape)
print(cbRecovered_.shape)
print(yRecovered_.shape)

# Unión de los canales Y (recuperado), Cr (recuperado), Cb (recuperado) 
imagen_final = cv2.merge([yRecovered_, crRecovered_, cbRecovered_])
imagen_final = cv2.cvtColor(imagen_final, cv2.COLOR_YCrCb2BGR)

# Guardar imagen RGB Final
cv2.imwrite('finalImageRGB.bmp', np.uint8(imagen_final))

# Mensaje recuperado
print("\nMensaje recuperado")
print(stgnP.stgn_out(matrixRecoveredR, T))

# Parametros finales
print("\nPARAMETROS FINALES")
psnr_final = pmt.calculate_psnr(file,'finalImageRGB.bmp')
print(f"PSNR_FINAL: {psnr_final} dB")
ssim_final = pmt.calculate_ssim(file,'finalImageRGB.bmp')
print(f"SSIM_FINAL: {ssim_final}")
print("\n")
