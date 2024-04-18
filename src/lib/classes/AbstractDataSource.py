#Uma classe abstrata é como se fosse um padrão obrigatório (um tipo de "amarra")
#que deverá ser seguido por outra classe quando a classe abstactDataSource for importada
#ou seja, todas as classes que importarem esta classe, obrigatoriamente deverá ser 
#implementado também a classe start, get_data, transform_data_to_df e save_data

from abc import ABC, classmethod

class AbstractDataSource(ABC):
    def __init__(self):
        pass
     
    @classmethod
    def start(self):
        raise NotImplementedError("Método não implementado")

    @classmethod
    def get_data(self):
        raise NotImplementedError("Método não implementado")

    @classmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Método não implementado")

    @classmethod
    def save_data(self):
        raise NotImplementedError("Método não implementado")

    def hello_world(self):
        print('Hello World')
    
