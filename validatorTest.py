import unittest

import validator


class TestValidator(unittest.TestCase):
    v = None

    def setUp(self):
        self.v = validator.Validator()

    def test_normal_url(self):
        url = "https://www.amazon.com.br/"
        self.assertTrue(self.v.is_url(url))

    def test_invalid_url(self):
        url = "asdfdghjkdfghkj"
        self.assertFalse(self.v.is_url(url))

    def test_empty_url(self):
        url = ""
        self.assertFalse(self.v.is_url(url))

    def test_not_http(self):
        url = "ftp://ftp.seusite.com.br"
        self.assertFalse(self.v.is_url(url))

if __name__ == '__main__':
    unittest.main()
