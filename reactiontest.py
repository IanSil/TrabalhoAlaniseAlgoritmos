from time import sleep
from interfaces import action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class Reaction(action):

    def __init__(self):
        self.__url = "https://www.wikipedia.org/"

    def trigger(self):
        print("Abrindo Wikipedia")
        driver = webdriver.Chrome()
        driver.get(self.__url)

        search = "Trabalho acadêmico"
        for letra in search:
            driver.find_element(By.ID, "searchInput").send_keys(letra)
            sleep(0.2)
        sleep(1)
        driver.find_element(By.CLASS_NAME, "pure-button-primary-progressive").click()

        try:
            while True:
                _ = driver.title
                sleep(1)
        except WebDriverException:
            print("Janela fechada pelo usuário")
        finally:
            driver.quit()
