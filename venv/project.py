from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get('https://web.whatsapp.com')

time.sleep(50)

message = """
  Versão teste de automação do whats!
  Deu certo! """

contacts_list = ["Edio", "Samuel Chaves Pai Da Luna", "Mae Novo"]

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Meu Numero")
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(1)

pyperclip.copy(message)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/div[1]/p').send_keys(Keys.CONTROL + 'v')
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)

elements_list = nav.find_elements('class name', '_2AOIt')
time.sleep(2)
for item in elements_list:
  message = message.replace("\n", "")
  text = item.text.replace("\n", "")
  if message in text:
    element = item
    break

ActionChains(nav).move_to_element(element).perform()
element.find_element('class name', '_3u9t-').click()
time.sleep(2000)





