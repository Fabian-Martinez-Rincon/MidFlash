<h1 align="center"> 🤖 MidFlash </h1>
<div align="center">
<img src="https://user-images.githubusercontent.com/55964635/209423757-dc0ee138-37e4-409d-a1f9-2f48c1da904e.png"/>
 </div>

<br>


### Version de Selenium 4.7.2

### Instalar dependencias

```cmd
pip install selenium
```

## Explicacion momentanea 

- `1)` El programa comienza leyendo la ruta de una imagen de entrada y cargándola en memoria.
- `2)` El programa utiliza una técnica de procesamiento de imagen, como el algoritmo de borde de Canny, para detectar los bordes de la imagen y determinar qué partes de la imagen deben recortarse.
- `3)` El programa recorta la imagen según los bordes detectados y almacena la imagen recortada en una variable.
- `4)` El programa utiliza un modelo de inteligencia artificial entrenado para aumentar la resolución de las imágenes para aumentar la resolución de la imagen recortada.
- `5)` El programa guarda la imagen con la resolución aumentada en una ruta de salida especificada por el usuario.
- `6)` El programa finaliza y muestra al usuario un mensaje de éxito o un mensaje de error en caso de que haya ocurrido algún problema durante el procesamiento.

### Links de ayuda

- [Libreria](https://www.selenium.dev/selenium/docs/api/py/)
- [Link para las Imagenes](https://zyro.com/es/herramientas/upscaler-de-imagenes)


### Apretar botones de una web

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)

    driver.get('https://fabianmartinez.vercel.app/')

    # get all buttons by common class
    buttons = driver.find_elements(By.CLASS_NAME, 'css-1v7r4tf')
    #print("Botones" , buttons[0])
    # wait for first button (buttons[0]) be clickable and click
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(buttons[0])).click()
    #time.sleep(3)
    
    input()
    # clicking in all buttons
    #for button in buttons:
    #    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button)).click()
    #    time.sleep(3)

    driver.quit()
```

### Codigo Para recortar todas las imagenes

```python
import os
from PIL import Image

PATH_BASE = os.getcwd()
PATH_SOURCE = os.path.join(PATH_BASE, "base_images")
PATH_PROSSED = os.path.join(PATH_BASE, "processed_images")

if not os.path.exists(PATH_PROSSED):
    os.makedirs(PATH_PROSSED, exist_ok=True)

def cutout(image):

    imagen = Image.open(os.path.join(PATH_SOURCE, image))
    
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
        
        imagen_cuadrante.save(
            os.path.join(
                PATH_PROSSED, 
                image.replace('.png', '_{}.jpg'.format(i))
                )
            )

```

# Recorre la lista de cuadrantes y crea una imagen para cada uno
```python
try:
    imagenes = [
        imagen for imagen in os.listdir(PATH_SOURCE) 
        if imagen.endswith(('.jpg', '.png'))
    ]
    for image in imagenes:
        cutout(image)
except FileNotFoundError:
    print('No existe la ruta', PATH_SOURCE)
except NotADirectoryError:
    print('La ruta no es un directorio ', PATH_SOURCE)
```