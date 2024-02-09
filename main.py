from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.bbc.com/news")


wait = WebDriverWait(navegador, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gs-c-promo-heading")))

news_elements = navegador.find_elements(By.CLASS_NAME, "gs-c-promo-heading")


for index, news_element in enumerate(news_elements, start=1):
    if news_element.text == ("").strip() or news_element.text == ("VIDEO").strip():
        pass
    else:
        print(f"Notícia {index}: {news_element.text}")

time.sleep(5)
