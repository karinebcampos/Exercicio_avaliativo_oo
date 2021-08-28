from discos import Discos
from artistas import Artistas
from genero import Genero

class Main:

    def __init__(self):
        self.discos = Discos()
        self.discos.set_titulosdiscos('Novo Disco')
        self.discos.set_ano(2021)
        self.__discos = []
        self.__artistas = []
        self.__genero = []

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

    def cadastrar_discos(self):
        titulodisco = input('Digite o título do disco: ')
        ano = input('Digite o ano em que o disco foi lançado: ')
        discos = Discos(titulodisco, ano)
        self.__titulodiscos.append(discos)


    def listar_discos(self):
        for id, discos in enumerate(self.__discos):
            print(str(id) + 'nome ' + discos.get_titulosdiscos() +
                  'email' + discos.get_ano())


    def executar(self):
        while True:
            self.mostrar_menu()
            opcao = input('Digite a opção desejada: ')
            print(opcao)
        if opcao == '1':
            self.cadastrar_artista()
        elif opcao == '2':
            self.excluir_artista()
        elif opcao == '3':
            self.cadastrar_genero()
        elif opcao == '4':
            self.excluirgenero()
        elif opcao == '5':
            self.cadastrar_discos()
        elif opcao == '6':
            self.excluirdisco()
        elif opcao == '7':
            self.listartodososdiscos()
        elif opcao == '8':
            self.listardiscosgenero()
        elif opcao == '9':
            self.listardiscosartistas()





Main().executar()
