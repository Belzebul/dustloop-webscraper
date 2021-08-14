from bs4 import BeautifulSoup
import json

class DictBuilder:
    DUSTLOOP_DOMAIN = 'https://dustloop.com'
    
    def mount(self, table_body, columns):
        table_rows = table_body.find_all('tr')
        dict_rows = {}
        
        for row in table_rows:
            dict_cells = self.mount_rows(row, columns)
            if 'sprite' in columns:
                dict_cells['sprite'] = self.get_sprite_url(row)
            
            key = dict_cells['input'] if 'input' in dict_cells.keys() else dict_cells['name']
            dict_rows.update({key: dict_cells})

        return dict_rows


    def mount_rows(self, row, columns):
        INDEX_COLUMNS = range(0, len(columns))
        cells = row.find_all('td')
        dict_cells = {}

        for index in INDEX_COLUMNS:
            key = columns[index]
            value = cells[index].get_text()
            dict_cells.update({key: value})

        return dict_cells


    def get_sprite_url(self, tr_tag):
        hidden_tag = BeautifulSoup(tr_tag['data-details'],'html.parser')
        img_tag = hidden_tag.find('img')
        url = self.DUSTLOOP_DOMAIN + img_tag['src']
        return url
