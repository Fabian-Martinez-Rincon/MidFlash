
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)

    driver.get('https://zyro.com/es/herramientas/upscaler-de-imagenes')


    buttons = driver.find_elements(By.CLASS_NAME, 'button.medium-up.button--small.button--small-mobile.button--black')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(buttons[0])).click()
    
    
    buttons = driver.find_elements(By.CLASS_NAME, 'button.hero__button.button--small.button--small-mobile.button--white')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(buttons[0])).click()
    
    #time.sleep(3)
    
    input()
    # clicking in all buttons
    #for button in buttons:
    #    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button)).click()
    #    time.sleep(3)

    driver.quit()