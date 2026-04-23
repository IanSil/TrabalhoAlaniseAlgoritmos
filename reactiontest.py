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
        self.driver = webdriver.Chrome()
        self.driver.get(self.__url)

        search = "Trabalho acadêmico"
        for letra in search:
            self.driver.find_element(By.ID, "searchInput").send_keys(letra)
            sleep(0.2)
        sleep(1)
        self.driver.find_element(
            By.CLASS_NAME, "pure-button-primary-progressive"
        ).click()

        try:
            while True:
                _ = self.driver.title
                sleep(1)
        except WebDriverException:
            print("Janela fechada pelo usuário")
        finally:
            self.driver.quit()

    def close_driver(self):
        if self.driver:
            try:
                self.driver.quit()
                print("Driver encerrado com sucesso.")
            except Exception as e:
                print(f"Erro ao tentar fechar o driver: {e}")
            finally:
                self.driver = None
