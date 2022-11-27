
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_automationlogIn():
    nombre = 'agus.aused@gmail.com'
    password = 'AgustinAused-'
    # url de la pagina para la automatizacion
    url = 'https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/'
    driver = webdriver.Chrome(r'\home\user\drivers\chromedriver')

    # entrar al sitio web
    driver.get(url)
    paginaLog = driver.find_element(By.LINK_TEXT, 'Sign In')
    paginaLog.click()
    driver.maximize_window()
    # esperar a que se cargeun los compenentes
    driver.implicitly_wait(3)

    # seleciona los campos
    driver.find_element(By.ID , 'email').send_keys(nombre)
    driver.find_element(By.ID , 'pass').send_keys(password)


    # seleciona el boton para ingresar
    submit_button = driver.find_element(By.ID, 'send2')
    submit_button.click()
    driver.quit()
def test_automationlogIn2():
    nombre = 'agus.aused@gmail.com'
    password = 'AgustinAused'
    # url de la pagina para la automatizacion
    url = 'https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly'
    driver = webdriver.Chrome(r'\home\user\drivers\chromedriver')
    # entrar al sitio web
    driver.get(url)
    driver.maximize_window()
    # esperar a que se cargeun los compenentes
    driver.implicitly_wait(3)
    # seleciona los campos
    driver.find_element(By.ID , 'email').send_keys(nombre)
    driver.find_element(By.ID , 'pass').send_keys(password)
    # seleciona el boton para ingresar
    submit_button = driver.find_element(By.ID, 'send2')
    submit_button.click()
    driver.implicitly_wait(5)
    driver.quit()


