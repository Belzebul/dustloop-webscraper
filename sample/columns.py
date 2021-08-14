from enum import IntEnum

from html_data_collector import HTMLFramedataCollector

class Columns(IntEnum):
    SYSTEM_DATA = 0
    NORMALS = 1
    SPECIALS = 2
    SUPERS = 3
    OTHERS = 4


class ColumnsBuilder():

    def __init__(self, html_data):
        self.html_data = html_data


    def get_columns(self, table):
        thead_tag = self.html_data.get_thead(table)
        th_tag_list = thead_tag.find_all('th')
        columns = []

        for th in th_tag_list:
            columns.append(th.get_text())

        if (columns[0] == ''): 
            columns[0] = 'sprite'

        return columns


if __name__ == '__main__':
    html_data_collector = HTMLFramedataCollector('https://www.dustloop.com/wiki/index.php?title=GGST/Nagoriyuki/Frame_Data')
    columns = ColumnsBuilder(html_data_collector)
    colunas = columns.get_columns(Columns.NORMALS)
    print(colunas)
