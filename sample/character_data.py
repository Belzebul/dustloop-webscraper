import json
from dict_builder import DictBuilder
from html_data_collector import HTMLFramedataCollector
from columns import Columns, ColumnsBuilder

class CharacterData():

    def __init__(self, url_character):
        self.html_data = HTMLFramedataCollector(url_character)
        self.dict_builder = DictBuilder()
        self.character = {}

    def build(self):
        dict_list = self.mount_dicts(self.dict_builder)
        moves = self.concat_dicts(dict_list)

        return {'nagoriyuki': moves} #hardcoded

    def mount_dicts(self, dict_builder):
        colBuilder = ColumnsBuilder(self.html_data)
        dict_moves = ['']*5

        for table_id in Columns:
            cols = colBuilder.get_columns(table_id)
            dict_moves[table_id] = dict_builder.mount(self.html_data.get_tbody(table_id), cols)

        return dict_moves

    def concat_dicts(self, dict_list):
        dict_character = {}
        for d in dict_list: 
            dict_character.update(d)
        return dict_character


if __name__ == '__main__':
    character = CharacterData('https://www.dustloop.com/wiki/index.php?title=GGST/Nagoriyuki/Frame_Data')
    char_dict = character.build()

    with open('test_json.json', 'w') as file:
        json.dump(fp=file, obj=char_dict)