import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


class Selection:

    def __init__(self, url):

        self.__url = url
        self.__xpath = ""
        self.__conteudo = ""
        driver = webdriver.Chrome()
        js_script = """
        window.selectedElement = null;

        function getXPath(element) {

            if (element.id !== '')
                return 'id("' + element.id + '")';
            if (element === document.body)
                return element.tagName;

            var ix = 0;
            var siblings = element.parentNode.childNodes;
            for (var i = 0; i < siblings.length; i++) {
                var sibling = siblings[i];
                if (sibling === element)
                    return getXPath(element.parentNode) + '/' + element.tagName + '[' + (ix + 1) + ']';
                if (sibling.nodeType === 1 && sibling.tagName === element.tagName)
                    ix++;
            }
        }

        document.addEventListener('mouseover', function(e) {
            e.target.style.outline = '2px dashed blue';
        }, false);

        document.addEventListener('mouseout', function(e) {
            e.target.style.outline = '';
        }, false);

        document.addEventListener('click', function(e) {
            e.preventDefault();
            window.selectedElement = {
                xpath: getXPath(e.target),
                text: e.target.innerText
            };
        }, false);
        """

        driver.get(self.url)
        driver.execute_script(js_script)

        print("Selecionando um elemento")

        try:
            while True:
                result = driver.execute_script("return window.selectedElement;")
                if result:
                    self.__xpath = result["xpath"]
                    self.__conteudo = result["text"]
                    print("\n--- Captura Concluída ---")
                    print(f"XPath: {self.xpath}")
                    print(f"Conteúdo atual: {self.conteudo}")
                    break
                time.sleep(0.5)
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

    @property
    def url(self):
        return self.__url

    @property
    def xpath(self):
        return self.__xpath

    @property
    def conteudo(self):
        return self.__conteudo

    def como_dicionario(self):
        return {"url": self.__url, "xpath": self.__xpath, "conteudo": self.__conteudo}

    def __str__(self):
        return f"Seleção em: {self.__url}\nXPath: {self.__xpath}\nTexto: {self.__conteudo}"
