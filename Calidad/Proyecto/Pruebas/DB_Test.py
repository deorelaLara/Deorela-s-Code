import unittest
from APOD_Implement import *
from APOD_Abs import *
from Photo import *
from APOD_Implement import getPicture


# Implementamos la interfaz de la BD en la clase mock
class MockAPOD(DBService):
    #Manipulamos la informacion manual 
    def getInfo(self, date, title, explanation, url, media_type):
        self.photo = Photo(date, title, explanation, url, media_type)
    # Buscamos la info en la clase del mock y no en la funcion original del API
    def SearchPicture(self, date):
        return self.photo
