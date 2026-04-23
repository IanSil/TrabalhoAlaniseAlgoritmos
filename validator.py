from urllib import parse


class Validator:
    """
    Valida strings do programa
    """
    def is_url(self, url: str) -> bool:
        """
        :param url: string contendo algo que pode ou não ser uma url com endereço http
        :return: bool
        """
        return parse.urlparse(url).scheme in ['http', 'https'] and parse.urlparse(url).geturl() is not None
