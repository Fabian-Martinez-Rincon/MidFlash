from selenium import webdriver

# Para usar Chrome:
driver = webdriver.Chrome()
driver.get("https://fabianmartinez.vercel.app")

input('Presiona "enter" para cerrar el navegador')

# Cierra el navegador
driver.quit()