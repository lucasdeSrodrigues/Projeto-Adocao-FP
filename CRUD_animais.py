animais = []

def adicionar_animais():
    animal = {
        'nome': input('Digite o nome do animal: '),
        'especie': input('Digite a espécie do animal: '),
        'raca': input('Digite a raça do animal: '),
        'idade': int(input('Digite a idade do animal: ')),
        'saúde': input('Digite o estado de saúde do animal: '),
        'data de chegada': input('Digite a data de chegada do animal: '),        
        'comportamento': input('Digite o comportamento do animal: ')
    }
    animais.append(animal)
    print('Animal adicionado')


def visualizar_animais():
    if not animais:
        print('Nenhum animal cadastrado')
    else:
        for i, animal in enumerate(animais):
            print(f"{i + 1}. {animal['nome']} - {animal['especie']} - {animal['raca']} - {animal['idade']} anos - {animal['saúde']} - {animal['data de chegada']} - {animal['comportamento']}")


def editar_animais():
    visualizar_animais()
    if not animais:
        return
    try:
        indice = int(input('Digite o número do animal que deseja editar: ')) - 1

        if 0 <= indice and indice < len(animais):
            animal = animais[indice]
            
            novo_nome = input(f"Digite o novo nome do animal (atual: {animal['nome']}): ")
            if novo_nome.strip():
                animal['nome'] = novo_nome
            
            nova_especie = input(f"Digite a nova espécie do animal (atual: {animal['especie']}): ")
            if nova_especie.strip():
                animal['especie'] = nova_especie

            nova_raca = input(f"Digite a nova raça do animal (atual: {animal['raca']}): ")
            if nova_raca.strip():
                animal['raca'] = nova_raca

            nova_idade = input(f"Digite a nova idade do animal (atual: {animal['idade']}): ")
            if nova_idade.strip():
                animal['idade'] = int(nova_idade)

            novo_estado_saude = input(f"Digite o novo estado de saúde do animal (atual: {animal['saúde']}): ")
            if novo_estado_saude.strip():
                animal['saúde'] = novo_estado_saude

            nova_data_chegada = input(f"Digite a nova data de chegada do animal (atual: {animal['data de chegada']}): ")
            if nova_data_chegada.strip():
                animal['data de chegada'] = nova_data_chegada

            novo_comportamento = input(f"Digite o novo comportamento do animal (atual: {animal['comportamento']}): ")
            if novo_comportamento.strip():
                animal['comportamento'] = novo_comportamento

            print('Animal editado')
        else:
            print('Número inválido')
    except ValueError:
        print('Entrada inválida. Digite um número válido.')


def excluir_animais():
    visualizar_animais()
    if not animais:
        return
    try:
        indice = int(input('Digite o número do animal que deseja excluir: ')) - 1

        if 0 <= indice and indice < len(animais):
            del animais[indice]
            print('Animal excluído')
        else:
            print('Número inválido')
    except ValueError:
        print('Entrada inválida. Digite um número válido.')

while True:
    print('\nEscolha uma opção:')
    print('1. Adicionar animal')
    print('2. Visualizar animais')
    print('3. Editar animal')
    print('4. Excluir animal')
    print('5. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        adicionar_animais()
    elif opcao == '2':
        visualizar_animais()
    elif opcao == '3':
        editar_animais()
    elif opcao == '4':
        excluir_animais()
    elif opcao == '5':
        print('Saindo do programa. Até a próxima!')
        break
    else:
        print('Opção inválida. Tente novamente.')