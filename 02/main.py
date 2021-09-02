from conta_poupanca import Conta_Poupanca
from conta_corrente import Conta_Corrente


while True:
    print('---------------------------')
    print('Caixa Eletrônico')
    print('---------------------------')
    print('Qual conta você deseja acessar?')
    print('1 - Conta Corrente')
    print('2 - Conta Poupança')
    print('3 - Sair')
    escolher_tipo_de_conta = int(input('Insira o tipo de conta: '))

    if escolher_tipo_de_conta == 1:
        agencia_conta_corrente = int(input("Qual a agência da conta? "))
        conta_conta_corrente = input('Qual o número da conta? ')
        saldo_conta_corrente = float(input('Qual o saldo da conta? '))
        limite_conta_corrente = float(input('Qual o limite da conta? '))
        conta_corrente = Conta_Corrente(agencia_conta_corrente, conta_conta_corrente, saldo_conta_corrente, limite_conta_corrente)
        print()

        print('Que operação deseja fazer? ')
        print('1 - Depositar')
        print('2 - Sacar')
        print('3 - Sair')
        escolher_conta_corrente = int(input('O que deseja fazer? '))

        if escolher_conta_corrente == 1:
            valor_deposito_conta_corrente = float(input('Quanto deseja depositar? '))
            conta_corrente.depositar(valor_deposito_conta_corrente)


        elif escolher_conta_corrente == 2:
            valor_saque_conta_corrente = float(input('Quanto deseja sacar? '))
            conta_corrente.sacar(valor_saque_conta_corrente)


        elif escolher_conta_corrente == 3:
            print('Saindo')

        else:
            print('Insira uma opção válida!')

    if escolher_tipo_de_conta == 2:
        agencia_conta_poupanca = int(input('Qual a agência da conta? '))
        conta_conta_poupanca = input('Qual o número da conta? ')
        saldo_conta_poupanca = float(input('Qual o saldo da conta? '))
        conta_poupanca = Conta_Poupanca(agencia_conta_poupanca, conta_conta_poupanca, saldo_conta_poupanca)

        print('Que operação deseja fazer? ')
        print('1 - Depositar')
        print('2 - Sacar')
        print('3 - Sair')
        escolher_conta_poupanca= int(input('O que deseja fazer? '))


        if escolher_conta_poupanca == 1:
            valor_deposito_conta_poupanca = float(input('Quanto deseja depositar? '))
            conta_poupanca.depositar(valor_deposito_conta_poupanca)

        elif escolher_conta_poupanca == 2:
            valor_saque_conta_poupanca = float(input('Quanto deseja sacar? '))
            conta_poupanca.sacar(valor_saque_conta_poupanca)

        elif escolher_conta_poupanca == 3:
            print('Saindo')

        else:
            print('Insira uma opção válida!')

    if escolher_tipo_de_conta == 3:
        print('Saindo')

    else:
        print("Insira uma opção válida!")



