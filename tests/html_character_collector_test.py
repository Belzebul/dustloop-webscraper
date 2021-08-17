import unittest
from context import src

URL_CHARACTER: str = 'https://www.dustloop.com/wiki/index.php?title=GGST/Nagoriyuki/Frame_Data'

class HTMLCharacterCollectorTest(unittest.TestCase):
    '''Test the funcionalities of the HTMLDataCollector class'''

    def setUp(self):
        self.htmlCharacterCollector = src.CharacterHTMLCollector(URL_CHARACTER)

    def test_load_data(self):
        http_request = self.htmlCharacterCollector.load_data(URL_CHARACTER)
        self.assertEqual(http_request.status_code, 200)
    
    def test_parse_tables(self):
        tbody_list = self.htmlCharacterCollector.tbody_list
        self.assertGreaterEqual(len(tbody_list), 5)
    
if __name__ == '__main__':
    unittest.main()