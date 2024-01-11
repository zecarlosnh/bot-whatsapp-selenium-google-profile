from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
from time import sleep


options = Options()
options.add_argument("user-data-dir=C:\\Users\\ZeCar\\AppData\\Local\Google\\Chrome\\User Data")
options.add_argument('--profile-directory=Default')

driver = options
driver = webdriver.Chrome(options=options)

contato = ('5551999999999',)

driver.get('https://web.whatsapp.com')
sleep(20)
for i in contato:
    campo_pesquisa = driver.find_element('xpath', '//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[5]/div/span')
    sleep(2)
    campo_pesquisa.click()
    sleep(2)
    campo_pesquisa = driver.find_element('xpath', '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p')

    campo_pesquisa.send_keys(i)
    sleep(2)
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(2)
    campo_pesquisa = driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    campo_pesquisa.send_keys('teste')
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(2)
