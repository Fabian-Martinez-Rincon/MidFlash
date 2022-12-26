
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui

import time

from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)

    driver.get('https://zyro.com/es/herramientas/upscaler-de-imagenes')


    buttons = driver.find_elements(By.CLASS_NAME, 'button.medium-up.button--small.button--small-mobile.button--black')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(buttons[0])).click()
    
    button = driver.find_element(By.CLASS_NAME, 'button.hero__button.button--small.button--small-mobile.button--white')
    
    elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button)).click()
    time.sleep(3)
    pyautogui.write("C:\\Users\\fabian\\Desktop\\Imagenes\\Midjourney\\Recortadas\\Elegidas\\1.png")

    # Apreta la tecla Enter para seleccionar el archivo
    pyautogui.press("enter")
    time.sleep(10)
    ruta = "C:\\Users\\fabian\\Desktop\\Imagenes"
   
        
    button2 = driver.find_element(By.CLASS_NAME, 'button.button--medium.button--medium-mobile.button--black')
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button2)).click()
    #time.sleep(3)
    #opcion.send_keys("C:\\Users\\fabian\\Desktop\\MidFlash\\processed_images\\1_0.jpg")
    
    #time.sleep(3)
    
    input()
    # clicking in all buttons
    #for button in buttons:
    #    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button)).click()
    #    time.sleep(3)

    driver.quit()