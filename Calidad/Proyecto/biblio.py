from abc import ABC, abstractclassmethod

#interfaz
class PhotoBiblio(ABC):
    @abstractclassmethod
    def search(date):
        pass
    @abstractclassmethod
    def delete(date):
        pass
    @abstractclassmethod
    def insert(date):
        pass
