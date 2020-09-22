from models import *
from character import Personaje


def main():
    info = Personaje()
    data = info.getCharacter()

    for x in data:
        try:
            raw = x
            
            if raw:
                char, created = Characters.get_or_create(**raw)
                print(f"Character {'Created' if created else 'Existing'}:{char.name}")
        
        except Exception as error:
            print(error)

    

if __name__ =='__main__':
    main()
    myDB.close()