from artistas import Artistas
from genero import Genero

class Discos:

    def __init__(self):
        self.__titulodisco = ''
        self.__ano = 0
        self.__artistas = []
        self.__genero = []

    def get_titulodiscos(self):
        return self.__titulodisco

    def set_titulosdiscos(self, titulo):
        self.__titulodisco = titulo

    def add_titulosdiscos(self, titulo):
        self.__titulodisco.append(titulo)

    def remover_titulosdiscos(self, titulo):
        self.__titulodisco.remove(titulo)

    def get_titulosdiscos(self, posicao_titulo):
        return self.__titulodisco[posicao_titulo]

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_genero(self):
        return self.__genero

    def add_genero(self, genero):
        self.__genero.append(genero)

    def remover_genero(self, genero):
        self.__genero.remove(genero)

    def get_genero(self, posicao_genero):
        return self.__genero[posicao_genero]

    def get_artistas(self):
        return self.__artistas

    def add_artistas(self, artista):
        self.__artistas.append(artista)

    def remover_artistas(self, artista):
        self.__artistas.remove(artista)

    def get_artista(self, posicao_artista):
        return self.__artistas[posicao_artista]








