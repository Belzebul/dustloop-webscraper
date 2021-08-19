from enum import IntEnum
import json
import character_dict_builder
from character_html_collector import CharacterHTMLCollector

class TableName(IntEnum):
    SYSTEM_DATA = 0
    NORMALS = 1
    SPECIALS = 2
    SUPERS = 3
    OTHERS = 4
    

class CharacterService():

    def __init__(self, url_character, name):
        self.html_data = CharacterHTMLCollector(url_character)
        self.name = name
        self.character = {}


    def build(self):
        moves_dict = self.mount_moves_dicts()
        return {self.name: moves_dict}


    def mount_moves_dicts(self):
        moves_dict = {}

        for table_id in TableName:
            columns_name = self.get_columns(table_id)
            html_tbody = self.html_data.get_tbody(table_id)
            moves = character_dict_builder.build(html_tbody, columns_name)
            moves_dict.update(moves)

        return moves_dict


    def get_columns(self, table_id):
        thead_tag = self.html_data.get_thead(table_id)
        th_tag_list = thead_tag.find_all('th')
        columns = []

        for th in th_tag_list:
            columns.append(th.get_text())

        if (columns[0] == ''): 
            columns[0] = 'sprite'

        return columns


if __name__ == '__main__':
    character = CharacterService('https://www.dustloop.com/wiki/index.php?title=GGST/Nagoriyuki/Frame_Data')
    char_dict = character.build()

    with open('nagoriyuki_example.json', 'w') as file:
        json.dump(fp=file, obj=char_dict, indent=4)