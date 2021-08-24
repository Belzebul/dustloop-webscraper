import json
import os
import re
import ggst_url_collector
from character_service import CharacterService

def main():
    characters_urL_list = ggst_url_collector.get_characters_url()
    load_characters(characters_urL_list)


def load_characters(characters_urL_list):
    for character_url in characters_urL_list:
        character_name = find_character_name(character_url)
        try:
            character_service = CharacterService(character_url, character_name)
            character_dict = character_service.build()
            writer_character(character_name, character_dict) #hardcoded
        except:
            print(character_name + ' não foi encontrado!')

def find_character_name(character_url):
    #name = re.search('GGST\/([\s\S]*)\/Frame_Data',character_url)
    url_split = re.split('/', character_url)
    return url_split[5]

def writer_character(character_name, character_dict):
    url = 'GGST/{name}.json'.format(name = character_name)
    os.makedirs(os.path.dirname(url), exist_ok=True)
    with open(url, 'w') as file:
        json.dump(fp=file, obj=character_dict, indent=4)

    print(url + " -> concluído!")


if __name__ == '__main__':
    main()