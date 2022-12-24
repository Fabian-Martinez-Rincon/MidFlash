import os
from PIL import Image

os.makedirs('cuadrantes', exist_ok=True)

PATH_BASE = os.getcwd()
print("base1"+PATH_BASE)
PATH_SOURCE = os.path.join(PATH_BASE, "base_images")
PATH_PROSSED = os.path.join(PATH_BASE, "processed_images")
if not os.path.exists(PATH_PROSSED):
    os.makedirs(PATH_PROSSED, exist_ok=True)

#imagen = Image.open('FabianMartinez_building_hause_steel_frame_b17e81f5-a8b3-4898-83b2-cef1c9e519bb.png')



def cutout(image):
    print(image)
    PATH_IMAGE = os.path.join(PATH_SOURCE, image)
    imagen = Image.open(PATH_IMAGE)
    
    ancho, alto = imagen.size
    ancho_cuadrante = ancho // 2
    alto_cuadrante = alto // 2

    # Crea una lista con las coordenadas de cada cuadrante
    cuadrantes = [
        (0, 0, ancho_cuadrante, alto_cuadrante),
        (ancho_cuadrante, 0, ancho, alto_cuadrante),
        (0, alto_cuadrante, ancho_cuadrante, alto),
        (ancho_cuadrante, alto_cuadrante, ancho, alto)
    ]

    for i, cuadrante in enumerate(cuadrantes):
        # Utiliza el método crop() para cortar la imagen en el cuadrante especificado
        imagen_cuadrante = imagen.crop(cuadrante)
        ruta = os.path.join(PATH_PROSSED, 'imagen_cuadrante_{}.jpg'.format(i))
        # Guarda la imagen en el archivo
        imagen_cuadrante.save(ruta)



# Recorre la lista de cuadrantes y crea una imagen para cada uno


try:
    imagenes = [
        imagen for imagen in os.listdir(PATH_SOURCE) 
        if imagen.endswith(('.jpg', '.png'))
    ]
    print(imagenes)
    for image in imagenes:
        cutout(image)
except FileNotFoundError:
    print('No existe la ruta', PATH_SOURCE)
except NotADirectoryError:
    print('La ruta no es un directorio ', PATH_SOURCE)