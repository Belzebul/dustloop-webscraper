import requests
from character_html_collector import RequestException
from bs4 import BeautifulSoup

FRAMEDATA_PARENT_DIV = 15
FRAMEDATA_DIV = 1
HTTP_OK = 200
DUSTLOOP_DOMAIN = 'https://dustloop.com'
GGST_FRAMEDATE_URL = 'https://dustloop.com/wiki/index.php?title=GGST/Frame_Data'


def get_characters_url():
    http_content: bytes = load_data(GGST_FRAMEDATE_URL).content
    tag_a_list = find_tag_a_list(http_content)
    url_list = mount_url_list(tag_a_list)
    return url_list


def load_data(URL):
        http_request = requests.get(URL)
        if( http_request.status_code != HTTP_OK):
            raise RequestException(URL)

        return http_request


def find_tag_a_list(http_content: bytes):
    soup = BeautifulSoup(http_content, 'html.parser')
    div_tag_list = soup.findAll('div')
    framedata_div_list = div_tag_list[FRAMEDATA_PARENT_DIV].contents
    framedata_a_list = framedata_div_list[FRAMEDATA_DIV].findAll('a')
    
    return framedata_a_list


def mount_url_list(framedata_a_list):
    framedata_url_list = []
    for a in framedata_a_list:
        character_url = DUSTLOOP_DOMAIN + a['href']
        framedata_url_list.append(character_url)

    return framedata_url_list


if __name__ == '__main__':
    print(get_characters_url())