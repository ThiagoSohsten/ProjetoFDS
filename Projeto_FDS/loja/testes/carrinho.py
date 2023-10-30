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
sleep(2)
navegador.find_element('xpath','/html/body/header/div/a[4]').click()
sleep(2)
navegador.find_element('xpath','/html/body/div/a').click()
sleep(2)

#adicionando tudo no carrinho
navegador.find_element('xpath','/html/body/div/div[1]/button/a').click()
sleep(2)
navegador.find_element('xpath','/html/body/div/a[2]').click()
sleep(2)

navegador.find_element('xpath','/html/body/div/div[2]/button/a').click()
sleep(2)
navegador.find_element('xpath','/html/body/div/a[2]').click()
sleep(2)

navegador.find_element('xpath','/html/body/div/div[3]/button/a').click()
sleep(2)
navegador.find_element('xpath','/html/body/div/a[2]').click()
sleep(2)

navegador.find_element('xpath','/html/body/div/div[4]/button').click()
sleep(2)
navegador.find_element('xpath','/html/body/div/a[2]').click()
sleep(2)

navegador.find_element('xpath','/html/body/div/div[5]/button').click()
sleep(2)
navegador.find_element('xpath','/html/body/div/a[2]').click()
sleep(2)

navegador.find_element('xpath','/html/body/div/div[6]/button/a').click()
sleep(2)
#removendo 3 itens


navegador.find_element('xpath','/html/body/div/ul/div[1]/a').click()
sleep(1)
navegador.find_element('xpath','/html/body/div/ul/div[2]/a').click()
sleep(1)
navegador.find_element('xpath','/html/body/div/ul/div[3]/a').click()
sleep(1)
navegador.find_element('xpath','/html/body/div/ul/div[4]/a').click()
sleep(1)
navegador.find_element('xpath','/html/body/div/ul/div[5]/a').click()
sleep(1)
navegador.find_element('xpath','/html/body/div/ul/div[6]/a').click()
sleep(1)
navegador.find_element('xpath','/html/body/div/a').click()
sleep(2)