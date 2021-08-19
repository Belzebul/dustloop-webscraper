from character_service import CharacterService
import json

def main():
   character = CharacterService('https://www.dustloop.com/wiki/index.php?title=GGST/Nagoriyuki/Frame_Data')
   char_dict = character.build()
   with open('nagoriyuki_example.json', 'w') as file:
       json.dump(fp=file, obj=char_dict, indent=4)

if __name__ == '__main__':
    main()