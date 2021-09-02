

class Conta():
    def __init__(self, agencia, conta, saldo):
        self._agenda = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agenda

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('O valor do saldo precisa ser númerico')
        self._saldo = valor


    def depositar(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('O valor do depósito precisa ser numérico')
        self._saldo += valor
        self.detalhes()


    def detalhes(self):
        print(f'Agência -> {self.agencia}', end=' ')
        print(f'Conta -> {self.conta}', end=' ')
        print(f'Saldo -> {self.saldo}')


    def sacar(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('O valor do saque precisa ser númerico')
        self.saldo += valor
        self.detalhes()




