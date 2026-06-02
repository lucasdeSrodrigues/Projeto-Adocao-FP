animais = []

def adicionar_animais():
    animal = {
        'nome': input('Digite o nome do animal: '),
        'especie': input('Digite a espécie do animal: '),
        'raca': input('Digite a raça do animal: '),
        'idade': int(input('Digite a idade do animal: ')),
        'saude': input('Digite o estado de saúde do animal: '),
        'data_chegada': input('Digite a data de chegada do animal: '),        
        'comportamento': input('Digite o comportamento do animal: ')
    }
    animais.append(animal)
    print('Animal adicionado com sucesso.')


def visualizar_animais():
    if not animais:
        print('Nenhum animal cadastrado.')
    else:
        for i, animal in enumerate(animais, start=1):
            print(f"{i}. {animal['nome']} - {animal['especie']} - {animal['raca']} - "
                  f"{animal['idade']} anos - {animal['saude']} - {animal['data_chegada']} - "
                  f"{animal['comportamento']}")


def editar_animais():
    visualizar_animais()
    if not animais:
        return
    try:
        indice = int(input('Digite o número do animal que deseja editar: ')) - 1
        if 0 <= indice < len(animais):
            animal = animais[indice]
            for campo in animal.keys():
                novo_valor = input(f"Novo {campo} (atual: {animal[campo]}): ")
                if novo_valor.strip():
                    animal[campo] = int(novo_valor) if campo == 'idade' else novo_valor
            print('Animal editado com sucesso.')
        else:
            print('Número inválido.')
    except ValueError:
        print('Entrada inválida. Digite um número válido.')


def excluir_animais():
    visualizar_animais()
    if not animais:
        return
    try:
        indice = int(input('Digite o número do animal que deseja excluir: ')) - 1
        if 0 <= indice < len(animais):
            removido = animais.pop(indice)
            print(f"Animal '{removido['nome']}' excluído com sucesso.")
        else:
            print('Número inválido.')
    except ValueError:
        print('Entrada inválida. Digite um número válido.')


def menu():
    while True:
        print('\n=== Sistema de Cadastro de Animais ===')
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
            print('Saindo do programa.')
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()