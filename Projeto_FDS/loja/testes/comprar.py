from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('http://127.0.0.1:8000/')
sleep(3)
navegador.find_element('xpath', '/html/body/header/div/a[2]').click()
sleep(2)
navegador.find_element('xpath', '//*[@id="id_username"]').send_keys("steve")
sleep(2)
navegador.find_element('xpath', '//*[@id="id_password"]').send_keys("123")
sleep(2)
navegador.find_element('xpath', '//*[@id="id_email"]').send_keys("steve@gmail.com")
sleep(2)
navegador.find_element('xpath','/html/body/div/form/button').click()
sleep(2)

elemento_nicho = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="id_nicho"]'))
)
elemento_nicho.click()
sleep(2)

opcao_nicho = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="id_nicho"]/option[3]'))
)
opcao_nicho.click()
sleep(2)

navegador.find_element(By.XPATH, '/html/body/form/button').click()
sleep(2)


navegador.find_element(By.XPATH, '/html/body/header/div/a[4]').click()
sleep(2)

navegador.find_element(By.XPATH, '/html/body/div/a').click()
sleep(2)

navegador.find_element(By.XPATH, '/html/body/div/div[1]/button').click()
sleep(2)

navegador.find_element(By.XPATH, '/html/body/div/a[1]').click()
sleep(2)

navegador.find_element('xpath','//*[@id="id_numero"]').send_keys('2222222222222222')
sleep(2)
navegador.find_element('xpath','//*[@id="id_validade"]').send_keys('07/2023')
sleep(2)
navegador.find_element('xpath','//*[@id="id_cvv"]').send_keys('123')
sleep(2)
navegador.find_element('xpath','/html/body/form/button').click()
sleep(2)