"""
Algoritmo para la visualización del almacenamiento de datos con el Algortimo de Canny
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librería
# ------------------------------------------------------------------------------------------------------------------

from PIL import Image

# ------------------------------------------------------------------------------------------------------------------
# Función
# ------------------------------------------------------------------------------------------------------------------

def find_difference(image01,image02,image_out):
    img_01 = Image.open(image01)
    img_02 = Image.open(image02)

    pixels_01 = img_01.load()
    pixels_02 = img_02.load()

    size_ = img_01.size
    width = size_[0]
    height = size_[1]

    for x in range(width):
        for y in range(height):
            
            pixel_01 = pixels_01[x,y]
            pixel_02 = pixels_02[x,y]

            red1 = pixel_01[0]
            green1 = pixel_01[1]
            blue1 = pixel_01[2]

            red2 = pixel_02[0]
            green2 = pixel_02[1]
            blue2 = pixel_02[2]

            if(red1!=red2 or green1!=green2 or blue1!=blue2):
                pixels_02[x, y] = (255,0,0)

    img_02.save(image_out)

