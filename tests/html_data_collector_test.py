import unittest
from context import sample

class HTMLDataCollectorTest(unittest.TestCase):
    URL_CHARACTER = 'https://www.dustloop.com/wiki/index.php?title=GGST/Nagoriyuki/Frame_Data'
    htmlFrameDataCollector = sample.HTMLFramedataCollector(URL_CHARACTER)
    
    def test_load_data(self):
        http_request = self.htmlFrameDataCollector.load_data(self.URL_CHARACTER)
        self.assertEqual(http_request.status_code, 200)
    
    def test_parse_tables(self):
        http_request = self.htmlFrameDataCollector.load_data(self.URL_CHARACTER)
        tbody_list = self.htmlFrameDataCollector.parse_tbodys(http_request.content)
        self.assertGreaterEqual(len(tbody_list), 5)
    
if __name__ == '__main__':
    unittest.main()