from conta import Conta

class Conta_Corrente(Conta):
    def __init__(self, agenda, conta, saldo, limite):
        super().__init__(agenda, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite


    def sacar(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('Saldo precisa ser numérico')
        if(self._saldo + self._limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()

