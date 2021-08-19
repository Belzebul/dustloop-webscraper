from context import src
import unittest
import re

from bs4 import BeautifulSoup

SPECIALS_COLUMNS = ['sprite', 'input', 'name', 'damage', 'guard', 'startup', 'active', 'recovery', 'onBlock', 'onHit', 'riscGain', 'level', 'invuln', 'prorate']

class TestCharacterDictBuilder(unittest.TestCase):

    html_doc = ''

    def setUp(self) -> None:
        with open('html_input_test.txt', 'r') as reader:
            for line in reader.readlines():
                self.html_doc += line
        
        html_doc_no_spaces = re.sub('\\n','', self.html_doc)
        soup = BeautifulSoup(html_doc_no_spaces, 'html.parser')
        self.html_body = soup.find('tbody')


    def test_build(self):
        framedata_dict = src.character_dict_builder.build(self.html_body, SPECIALS_COLUMNS)
        special = framedata_dict['236S']
        self.assertEqual(special['name'], 'Zarameyuki')
        

if __name__ == '__main__':
    unittest.main()
