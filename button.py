
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 20:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds

def push_button(button, driver):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            driver.find_element(By.CLASS_NAME, button)
        )).click()


WEB = 'https://zyro.com/es/herramientas/upscaler-de-imagenes'
BUTTON_CLOSE = 'button-close.modal__close-button'
BUTTON_COOKIES = 'button.medium-up.button--small.button--small-mobile.button--black'
BUTTON_LOAD = 'button.hero__button.button--small.button--small-mobile.button--white'
BUTTON_DOWNLOAD = 'button.button--medium.button--medium-mobile.button--black'
BUTTON_NEWLOAD = 'button.button--outline.button--medium.button--medium-mobile.button--black'
IMAGE = 'C:\\Users\\fabian\\Desktop\\Imagenes\\Midjourney\\Recortadas\\Elegidas\\1.png'

PATH_DOWNLOAD = "C:\\Users\\fabian\\Downloads"

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
    driver.get(WEB)

    #Setup
    push_button(BUTTON_COOKIES, driver)
    push_button(BUTTON_LOAD, driver)
    
    time.sleep(3)
    
    pyautogui.write(IMAGE)
    pyautogui.press("enter")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, BUTTON_DOWNLOAD)))
    
    #time.sleep(10)
    
    push_button(BUTTON_DOWNLOAD, driver)
    os.system("cls")
    
    #-------------------------------
    
    push_button(BUTTON_NEWLOAD, driver)
    time.sleep(3)
    
    pyautogui.write(IMAGE)
    pyautogui.press("enter")
    
    time.sleep(15)
    push_button(BUTTON_DOWNLOAD, driver)
    
    
    download_wait(PATH_DOWNLOAD)
    driver.quit()



