from urllib import parse


class Validator:
    def is_url(self, url: str) -> bool:
        return parse.urlparse(url).scheme in ['http', 'https'] and parse.urlparse(url).geturl() is not None
