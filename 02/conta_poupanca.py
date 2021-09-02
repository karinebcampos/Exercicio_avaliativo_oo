from conta import Conta

class Conta_Poupanca(Conta):
    def sacar(self,valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O saldo precisa ser númerico')
        if self._saldo < valor:
            print('Saldo é insuficiente para completar operação')
            return

        self.saldo -= valor
        self.detalhes()
