class Conta:

    def __init__(self, cliente, saldo):

        self.cliente = cliente
        self.saldo = saldo


    def depositar (self, valor):
        if valor > 0:
            self.saldo += valor
            print('Foi depositado:', valor)
            print('Saldo total', self.saldo)
        else:
            print('Erro ao depositar, precisa ser maior que R$: 0,00')

    def sacar(self, valor):
        if self.saldo - valor < 0:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print("Foi sacado o valor de:", valor)
            print("Seu saldo agora é de:", self.saldo)


    def consulta_saldo(self):
        return self.saldo
