from discos import Discos
from artistas import Artistas
from genero import Genero

class Main:

    def __init__(self):
        self.__artistas = []
        self.__genero = []
        self.__disco = []


    def cadastrar_artistas(self):
        nome = input('Digite o nome do artista: ')
        artistas = Artistas(nome)
        self.__artistas.append(artistas)
        print('-------------------------------')
        print('Artista cadastrado com sucesso')


    def excluir_artistas(self):
        id = input('Digite o ID do artista que deseja excluir: ')
        self.__artistas.pop(int(id))
        print('Artista excluído')


    def cadastrar_genero(self):
        nome_genero = input('Digite o genero que deseja cadastrar: ')
        genero = Genero(nome_genero)
        self.__genero.append(genero)
        print('-----------------------------')
        print('Genero cadastrado com sucesso')


    def excluir_genero(self):
        id = input('Digite o ID do genero que deseja excluir: ')
        self.__genero.pop(int(id))
        print('Genero excluído')


    def cadastrar_disco(self):
        titulo = input('Digite o título do disco: ')
        ano = input('Digite o ano em que o disco foi lançado: ')
        discos = Discos(titulo, ano)
        self.__disco.append(discos)
        print('-----------------------------')
        print('Disco cadastrado com sucesso')


    def excluir_disco(self):
        id = input('Digite o ID do disco que deseja excluir: ')
        self.__disco.pop(int(id))
        print('Disco excluído')


    def listar_artistas(self):
        print('Lista de artistas:')
        for id, nomeartistas in enumerate(self.__artistas):
            print(str(id) + ' Nome do artista: ' + nomeartistas.get_nomeartista())


    def listar_genero(self):
        print('Lista de generos:')
        for id, nomegenero in enumerate(self.__genero):
            print(str(id) + ' Nome do genero: ' + nomegenero.get_genero())


    def listar_disco(self):
        for id, discos in enumerate(self.__disco):
            print(str(id) + ' Titulo do disco: ' + discos.get_titulodisco() +
                  ' Ano do disco: ' + discos.get_ano())


    def mostrar_menu(self):
        print('')
        print('------------------------')
        print('DISCOS, ARTISTAS E ANO')
        print('------------------------')
        print('1 - Cadastrar Artista')
        print('2 - Excluir Artista')
        print('3 - Cadastrar Genero')
        print('4 - Excluir Genero')
        print('5 - Cadastrar Disco')
        print('6 - Excluir Disco')
        print('7 - Listar todos os discos')
        print('8 - Listar todos os discos de uma genero')
        print('9 - Listar os discos de um artista')



    def executar(self):
        while True:
            self.mostrar_menu()
            print('------------------------')
            opcao = input('Digite a opção desejada: ')
            print(opcao)
            if opcao =='1':
                self.cadastrar_artistas()
            elif opcao =='2':
                self.excluir_artistas()
            elif opcao =='3':
                self.cadastrar_genero()
            elif opcao =='4':
                self.excluir_genero()
            elif opcao =='5':
                self.cadastrar_disco()
            elif opcao=='6':
                self.excluir_disco()
            elif opcao =='7':
                self.listar_disco()
            elif opcao =='8':
               self.listar_genero()
            elif opcao =='9':
                self.listar_artistas()






Main().executar()
