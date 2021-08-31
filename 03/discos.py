from artistas import Artistas
from genero import Genero

class Discos:

    def __init__(self, titulo, ano):
        self.__titulodisco = titulo
        self.__ano = ano
        self.__artistas = []
        self.__genero = []

    def get_titulodisco(self):
        return self.__titulodisco

    def set_titulosdisco(self, titulo):
        self.__titulodisco = titulo

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_artistas(self):
        return self.__artistas

    def set_artiras(self, artistas):
        self.__artistas = artistas









