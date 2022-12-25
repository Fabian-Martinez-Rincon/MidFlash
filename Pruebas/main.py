import os



# Asume que estás en la carpeta que quieres explorar
# y que todas las imágenes tienen una extensión válida (jpg, png, etc.)
carpeta = './images'
imagenes = [
    imagen 
    for imagen 
    in os.listdir(carpeta) 
    if imagen.endswith(('.jpg', '.png'))
    ]
print(imagenes)

