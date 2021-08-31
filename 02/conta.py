from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.__agenda = agencia
        self.__conta = conta
        self.__saldo = saldo


    def agencia(self):
        return self.__agenda


    def conta(self):
        return self.__conta

    def saldo(self):
        return self.__saldo

    def saldo(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('O valor do saldo precisa ser númerico')
        self.__saldo = valor


