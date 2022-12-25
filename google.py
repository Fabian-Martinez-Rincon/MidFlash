from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://fabianmartinez.vercel.app/')

elem = browser.find_element(By.CLASS_NAME, r'chakra-button css-1c8mrgk')._execute  # Find the search box
#elem.click()

#pdf_number=browser.find_element(By.CLASS_NAME,"gsr-list-header").#.text.replace(" Results for Documents","")
            


input()
browser.quit()