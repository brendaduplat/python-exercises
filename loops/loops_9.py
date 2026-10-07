print('Escolha uma das seguintes opções:\n 1 - adicionar número.\n 2 - ver lista de números.\n 3 - ver a soma os números.\n 4 - ver maior número.\n 5 - sair.')
lista_numeros = []
while True:
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        novo_numero = int(input('Escolha um número para adicionar a lista: '))
        lista_numeros.append(novo_numero) 
    elif opcao == '2':
        if lista_numeros:
            print(lista_numeros)
        else:
            print('A lista está vazia.')
    elif opcao == '3':
        if lista_numeros:
            print(sum(lista_numeros))
        else:
            print('A lista está vazia.')
    elif opcao == '4':
        if lista_numeros:
            print(max(lista_numeros))
        else:
            print('A lista está vazia.')
    elif opcao == '5':
        break
    else:
        print('Escolha uma opcao valida.')