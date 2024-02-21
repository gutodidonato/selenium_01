"""
    Preparação do webdriver para chrome
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


"""
    utilites de raspagem do selenium
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.bbc.com/news")

# toda semana mudam a classe dinâmica dos elementos
classe_elementos_heading = "ssrcss-afqep1-PromoLink"
classe_elementos_secundarios = "ssrcss-17zglt8-PromoHeadline"


wait = WebDriverWait(navegador, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, classe_elementos_heading)))
news_elements = navegador.find_elements(By.CLASS_NAME, classe_elementos_heading)
for index, news_element in enumerate(news_elements, start=1):
    if news_element.text == ("").strip() or news_element.text == ("VIDEO").strip():
        pass
    else:
        print(f"Notícia {index}: {news_element.text}")

"""
efetuando segunda raspagem
"""

print("\n Noticias secundárias: ")
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, classe_elementos_secundarios))
)
news_elements = navegador.find_elements(By.CLASS_NAME, classe_elementos_secundarios)
for index, news_element in enumerate(news_elements, start=1):
    if news_element.text == ("").strip() or news_element.text == ("VIDEO").strip():
        pass
    else:
        print(f"Notícia {index}: {news_element.text}")
time.sleep(5)
"""
    Melhorias  possíveis:
        -utilizar api de tradução
        -integrar isso com wpp e automatizar a execução
        -criar um checkup de rotina para verificar se as classes ainda existem?
"""
