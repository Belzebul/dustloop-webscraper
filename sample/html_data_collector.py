from bs4 import BeautifulSoup
from bs4.element import PageElement
import requests

class HTMLFramedataCollector:
    NORMALS = 1
    SPECIALS = 2
    SUPERS = 3
    OTHERS = 4

    def __init__(self, url_character):
        http_content = self.load_data(url_character).content
        self.tbody_list = self.parse_tables(http_content,'tbody')
        self.thead_list = self.parse_tables(http_content,'thead')


    def load_data(self, URL):
        http_request = requests.get(URL)
        if( http_request.status_code != 200 ):
            raise RequestException(URL)

        return http_request


    def parse_tables(self, http_content, tag):
        soup = BeautifulSoup(http_content, 'html.parser')
        return soup.findAll(tag)


    def get_tbody(self, index):
        return self.tbody_list[index]


    def get_thead(self, index):
        return self.thead_list[index]


class RequestException(Exception):
    """invalid url"""

    def __init__(self, url, message = 'invalid url: '):
        super().__init__(message + url)


if __name__ == '__main__':
    test_collector = HTMLFramedataCollector('https://www.dustloop.com/wiki/index.php?title=GGST/Nagoriyuki/Frame_Data')
    with open('html_test_specials.html', 'w') as file:
        file.write(test_collector.get_tbody_specials().prettify())
