import requests
import json

#url ='https://www.breakingbadapi.com/api/characters'
def getCharacter():
    req =requests.get('https://www.breakingbadapi.com/api/characters')
    res = req.json()
    inf = []
    for i in res:
        id = i['char_id']
        name = i['name']
        birthday = i['birthday']
        occupation = i['occupation']
        img = i['img']
        status = ['status']
        nickname = ['nickname']
        portrayed = ['portrayed']
        category = ['category']

        info = {
            'id': id, 'name': name, 
            'birthday': birthday, 'occupation': occupation, 
            'img': img, 'status': status,'nickname': nickname,
            'portrayed': portrayed, 'category': category}       
        inf.append(info)
    return inf


print(getCharacter())