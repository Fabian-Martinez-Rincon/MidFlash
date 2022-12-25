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
    buttons = driver.find_elements(By.CLASS_NAME, 'chakra-button.css-1c8mrgk')
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