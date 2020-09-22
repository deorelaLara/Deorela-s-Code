import requests
import Civilizations
import DB
from Civilizations import civilization

def getCivilizations():
    req = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations')
    res = req.json()
    data = Civilizations()
    #total = res['civilizations'][0]
    #data = civilization()
    for j in range(1, 19):
        res = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/{}'.format(j))
        result = res.json()
        #data = civilization(result['id'], result['name'], result['army_type'], result['expansion'])
        #print(data)
        num = result['id']
        nom = result['name']
        arm = result['army_type']
        exp = result['expansion']

        '''print(result['id'])
        print(result['name'])
        print(result['army_type'])
        print(result['expansion'])
        print('----------')
        #print(result) #si hace el request'''
        #DB.addCiv(data)
        
        '''
        for i in range(1, 18):
            civili = Civilizations.civilizations(i['id'], i['name'], i['army_type'], i['expansion'])
            print(civili['id'])
            print(civili['name'])
            print(civili['army_type'])
            print(civili['expansion'])
            print('-------------------')'''


getCivilizations()