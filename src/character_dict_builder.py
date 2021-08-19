from bs4 import BeautifulSoup

DUSTLOOP_DOMAIN = 'https://dustloop.com'


def build(html_tbody, columns_name):
    html_table_rows = html_tbody.find_all('tr')
    character_dict = html_table_to_dict(html_table_rows, columns_name)

    return character_dict


def html_table_to_dict(table_rows, columns_name):
    char_rows = {}

    for row in table_rows:
        cells_dict = html_row_to_dict(row, columns_name)
        if 'sprite' in columns_name:
            cells_dict['sprite'] = get_sprite_url(row)

        key = cells_dict['input'] if 'input' in cells_dict.keys() else cells_dict['name']
        char_rows.update({key: cells_dict})
    return char_rows


def html_row_to_dict(row, columns):
    INDEX_COLUMNS = range(0, len(columns))
    cells_html = row.find_all('td')
    cells_dict = {}

    for index in INDEX_COLUMNS:
        key = columns[index].strip()
        value = cells_html[index].get_text().strip()
        cells_dict.update({key: value})

    return cells_dict


def get_sprite_url(tr_tag):
    hidden_tag = BeautifulSoup(tr_tag['data-details'], 'html.parser')
    img_tag = hidden_tag.find('img')
    if img_tag is None:
        return ''
    
    url = DUSTLOOP_DOMAIN + img_tag['src']
    return url
