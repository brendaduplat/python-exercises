pessoas = {}
while True:
    print('CADASTRO DE PESSOAS\n 1 - Adicionar pessoa\n 2 - Ver pessoas cadastradas\n 3 - Ver média de idade\n 4 - Ver pessoa mais velha\n 5 - Buscar pessoa pelo nome\n 6 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        novo_nome = input('Digite o nome: ')
        nova_idade = int(input('Digite a idade: '))
        if novo_nome in pessoas:
            print('Pessoa já cadastrada.')
        else:
            pessoas[novo_nome] = nova_idade
    elif opcao == '2':
        if pessoas:
            for nome, idade in pessoas.items():
                print(f'{nome}: {idade} anos')
        else:
            print('Não há pessoas cadastradas ainda.')
    elif opcao == '3':
        if pessoas:
            media = sum(pessoas.values()) / len(pessoas)
            print(f'Média de idade: {media:.1f} anos')
        else:
            print('Não há pessoas cadastradas ainda.')
    elif opcao == '4':
        if pessoas:
            mais_velha_nome = max(pessoas, key=pessoas.get)
            print(f'Pessoa mais velha: {mais_velha_nome} - {pessoas[mais_velha_nome]} anos.')
        else:
            print('Não há pessoas cadastradas ainda.')
    elif opcao == '5':
        if pessoas:
            buscar_nome = input('Digite o nome da pessoa que deseja buscar: ')
            if buscar_nome in pessoas:
                print(buscar_nome, pessoas[buscar_nome])
            else:
                print('Essa pessoa ainda não foi cadastrada.')
        else:
            print('Não há pessoas cadastradas ainda.')
    elif opcao == '6':
        break
    else:
        print('Opção invalida, tente novamente.')