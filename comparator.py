from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


class Comparator:
    """
    Compara o elemento selecionado e dá trigger na classe Action.
    Também armazena o intervalo de cada comparação
    TODO: mover isso para o scheduler depois
    """
    def __init__(self, Selection, Action, interval):
        """
        :param selection: elemento selecionado na página
        :param action:
        :param interval: tempo de intervalo entre as seleções
        """
        self.__selection = Selection
        self.__interval = interval
        self.__action = Action
        self.__last_change_detected = Selection.conteudo

    def compare(self) -> None:
        """
        Configura a conexão com um navegador chromium instalado no pc do usuário
        """
        try:
            options = Options()
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(10)
            driver.get(self.__selection.url)

            element = driver.find_element("xpath", self.__selection.xpath)
            element_text = element.text
        except NoSuchElementException:
            print("Erro: O elemento selecionado não foi encontrado na página.")
        except TimeoutException:
            print("Erro: A página demorou demais para carregar")
        except WebDriverException:
            print("Erro: O navegador foi fechado ou perdeu a conexão.")
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário (Ctrl+C).")
        finally:
            driver.quit()
        print(f"\n[{datetime.now():%d/%m/%Y %H:%M:%S}]")
        print(f"Elemento encontrado: {element}\nConteúdo atual: {element_text}")
        print(f"Conteúdo gravado da seleção: {self.__selection.conteudo}")
        if element_text != self.__selection.conteudo:
            print(f"Última mudaça reconhecida: {self.__last_change_detected}")
            self.__last_change_detected = element_text
            print("Ativando ação")
            self.__action.trigger()

    def change_interval(self, interval) -> None:
        """
        Modifica o intervalo entre verificações da página
        :param interval: interval
        """
        self.__interval = interval

    def __str__(self):
        return f"Selection: {self.__selection}\nAction: {self.__action}\nInterval: {self.__interval} minutos\nLast change detected: {self.__last_change_detected}\n"

    @property
    def interval(self):
        return self.__interval

    @property
    def selection(self):
        return self.__selection

    @property
    def last_change_detected(self):
        return self.__last_change_detected

    @property
    def action(self):
        return self.__action
