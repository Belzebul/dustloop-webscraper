from typing import List
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests

HTTP_OK = 200
HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'https://www.dustloop.com/wiki/index.php?title=GGST/Frame_Data'}

class CharacterHTMLCollector:

    def __init__(self, url_character: str):

        http_content: bytes = self.load_data(url_character).content

        self.tbody_list = self.parse_tables(http_content, 'tbody')
        self.thead_list = self.parse_tables(http_content, 'thead')


    def load_data(self, URL):
        http_request = requests.get(URL, headers=HEADERS)
        if( http_request.status_code != HTTP_OK):
            raise RequestException(URL)

        return http_request


    def parse_tables(self, http_content: bytes, tag: str) -> List[Tag]:
        soup = BeautifulSoup(http_content, 'html.parser')
        return soup.findAll(tag)


    def get_tbody(self, index: int) -> Tag:
        return self.tbody_list[index]


    def get_thead(self, index: int) -> Tag:
        return self.thead_list[index]


class RequestException(Exception):
    '''invalid url'''

    def __init__(self, url, message = 'invalid url: '):
        super().__init__(message + url)


if __name__ == '__main__':
    url = 'https://www.dustloop.com/wiki/index.php?title=GGST/Nagoriyuki/Frame_Data'
    test_collector = CharacterHTMLCollector(url)
    print(test_collector.get_tbody(2).prettify())
    '''with open('html_test_specials.html', 'w') as file:
        file.write(test_collector.get_tbody(2).prettify())'''
