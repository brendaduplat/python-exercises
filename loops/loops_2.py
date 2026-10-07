print('Para: \nVer saldo: 1\nDepositar: 2\nSacar: 3\nSair: 0')
saldo = 1000
opcao = ''
limite = - 500
while opcao != '0':
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        print(saldo)
    elif opcao == '2':
        valor_desposito = int(input('Digite o valor que deseja depositar: '))
        if valor_desposito < 0:
            print('Valor invalido.')
        else:
            saldo += valor_desposito
    elif opcao == '3':
        valor_sacar = int(input('Digite o valor que deseja sacar: '))
        if valor_sacar < 0 or saldo - valor_sacar < limite:
            print('saldo insuficiente.')
        else:
            saldo -= valor_sacar
    elif opcao == '0':
        print('Operação finalizada.')
    else:
        print('Opção não encontrada.')