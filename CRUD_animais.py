animais = []

def adicionar_animais():
    animal = {
        'nome': input('Digite o nome do animal: '),
        'especie': input('Digite a espécie do animal(cachorro/gato): '),
        'raca': input('Digite a raça do animal: '),
        'idade': int(input('Digite a idade do animal: ')),
        'saúde': input('Digite o estado de saúde do animal(saudavel/em tratamento/deficiente/cadeirante/sem vacina): '),
        'data de chegada': input('Digite a data de chegada do animal: '),        
        'comportamento': input('Digite o comportamento do animal(calmo/agitado): ')
    }
    animais.append(animal)
    print('Animal adicionado')


def visualizar_animais():
    if not animais:
        print('Nenhum animal cadastrado')
        return False
    else:
        for i, animal in enumerate(animais):
            print(f"{i + 1}. {animal['nome']} - {animal['especie']} - {animal['raca']} - {animal['idade']} anos - {animal['saúde']} - {animal['data de chegada']} - {animal['comportamento']}")
            return True


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


cuidados = []

def adicionar_cuidado():
    if not animais:
        print('Nenhum animal cadastrado.')
        return

    print('\nAnimais cadastrados:')
    for i, animal in enumerate(animais, 1):
        print(f'{i}. {animal["nome"]}')

    try:
        indice = int(input('Escolha o número do animal: ')) - 1
        if not (0 <= indice < len(animais)):
            print('Número inválido.')
            return
    except ValueError:
        print('Entrada inválida. Digite um número.')
        return

    print('\nTipos de cuidado:')
    print('1. Vacina')
    print('2. Banho')
    print('3. Consulta veterinária')
    print('4. Treino')
    print('5. Outro')

    tipos = {'1': 'Vacina', '2': 'Banho', '3': 'Consulta veterinária', '4': 'Treino', '5': 'Outro'}
    tipo = tipos.get(input('Escolha o tipo: '))
    if not tipo:
        print('Opção inválida.')
        return

    cuidado = {
        'animal': animais[indice]['nome'],
        'tipo': tipo,
        'data': input('Data prevista (DD/MM/AAAA): '),
        'responsavel': input('Responsável: ')
    }
    cuidados.append(cuidado)
    print('Cuidado registrado com sucesso.')


def visualizar_cuidados():
    if not cuidados:
        print('Nenhum cuidado registrado.')
        return
    for i, c in enumerate(cuidados, 1):
        print(f'{i}. {c["animal"]} - {c["tipo"]} - {c["data"]} - {c["responsavel"]}')


def editar_cuidado():
    visualizar_cuidados()
    if not cuidados:
        return
    try:
        indice = int(input('Número do cuidado que deseja editar: ')) - 1
        if not (0 <= indice < len(cuidados)):
            print('Número inválido.')
            return
    except ValueError:
        print('Entrada inválida. Digite um número.')
        return

    cuidado = cuidados[indice]

    novo_tipo = input(f'Tipo (atual: {cuidado["tipo"]}): ')
    if novo_tipo.strip():
        cuidado['tipo'] = novo_tipo

    nova_data = input(f'Data prevista (atual: {cuidado["data"]}): ')
    if nova_data.strip():
        cuidado['data'] = nova_data

    novo_responsavel = input(f'Responsável (atual: {cuidado["responsavel"]}): ')
    if novo_responsavel.strip():
        cuidado['responsavel'] = novo_responsavel

    print('Cuidado editado com sucesso.')


def excluir_cuidado():
    visualizar_cuidados()
    if not cuidados:
        return
    try:
        indice = int(input('Número do cuidado que deseja excluir: ')) - 1
        if 0 <= indice < len(cuidados):
            cuidados.pop(indice)
            print('Cuidado excluído com sucesso.')
        else:
            print('Número inválido.')
    except ValueError:
        print('Entrada inválida. Digite um número.')


def menu_sugestoes_personalizadas(animais):
    nome_busca = input('Digite o nome do animal para buscar sugestões personalizadas: ')
    animal_encontrado = None
    for animal in animais:
        if animal['nome'].lower() == nome_busca.lower():
            animal_encontrado = animal
            break
    if animal_encontrado is None:
        print('Animal não encontrado')
        return
    sugestoes_adotante = []
    cuidados_especiais = []
    compatibilidade_com_outros_animais = []
    if animal_encontrado['idade'] <= 1:
        sugestoes_adotante.append("Tutores com tempo livre para gastar energia e educar (fase de crescimento).")
        cuidados_especiais.append("Acompanhamento estrito do esquema de vacinas para filhotes.")
    elif animal_encontrado['idade'] >= 8:
        sugestoes_adotante.append("Famílias ou pessoas mais velhas que buscam um pet calmo e companheiro.")
        cuidados_especiais.append("Alimentação com ração sênior e atenção a dores nas articulações.")
    else:
        sugestoes_adotante.append("Adapta-se bem a rotinas dinâmicas (famílias adultas).")

    if animal_encontrado['especie'].lower() == "gato":
        cuidados_especiais.append("O ambiente do adotante DEVE ter telas de proteção nas janelas.")
        compatibilidade_com_outros_animais.append("Geralmente toleram outros gatos se adaptados lentamente, mas cuidado com aves/roedores.")
    elif animal_encontrado['especie'].lower() == "cachorro":
        cuidados_especiais.append("Necessidade de passeios diários para gasto de energia e estímulo mental.")

    comportamento = animal_encontrado['comportamento'].lower().strip()
    if "agitado" in comportamento:
        sugestoes_adotante.append("Casas com quintal grande ou tutores que praticam corridas/caminhadas.")
        compatibilidade_com_outros_animais.append("Excelente para conviver com crianças ativas.")
    elif "calmo" in comportamento:
        sugestoes_adotante.append("Ambientes silenciosos e sem muita movimentação ou barulho excessivo.")
        compatibilidade_com_outros_animais.append("Pode se assustar com crianças muito pequenas; prefere ambientes tranquilos.")
    
    saude = animal_encontrado['saúde'].lower().strip()
    if "em tratamento" in saude:
        cuidados_especiais.append("Adoção especial: O tutor deve ser alertado sobre a continuidade do tratamento médico em casa.")
        cuidados_especiais.append(f"Observação médica atual: {animal_encontrado['saúde']}.")
        sugestoes_adotante.append("Pessoas com disponibilidade de tempo para administrar medicações nos horários corretos.")
   
    elif "deficiente" in saude or "cadeirante" in saude:
        cuidados_especiais.append("Ambiente plano, sem escadas altas ou pisos muito escorregadios.")
        sugestoes_adotante.append("Casas térreas ou apartamentos adaptados para mobilidade reduzida.")
        compatibilidade_com_outros_animais.append("Evitar convivência inicial com pets muito enérgicos que possam machucá-lo.")
    
    elif "sem vacina" in saude:
        cuidados_especiais.append("Agendar castração/vacinação antes de liberar em definitivo para o adotante.")
        compatibilidade_com_outros_animais.append("Manter isolado de outros animais não vacinados ou do sexo oposto no abrigo.")
        
    elif "saudável" in saude:
        cuidados_especiais.append("Manter a rotina preventiva padrão (check-up anual e vacinas em dia).")
    
    else:
        cuidados_especiais.append(f"Atenção ao prontuário registrado: '{animal_encontrado['saúde']}'. Avaliar com o veterinário antes da adoção.")

    print("\n" + "="*100)
    print(f"\t\t\t\tSugestões personalizadas para o animal '{animal_encontrado['nome']}':")
    print("="*100)

    print("\nSugestões de adotantes ideais:")
    for sugestao in sugestoes_adotante:
        print(f"- {sugestao}")

    print("\nCuidados especiais necessários:")
    for cuidado in cuidados_especiais:
        print(f"- {cuidado}")

    print("\nCompatibilidade com outros animais e crianças:")
    for compatibilidade in compatibilidade_com_outros_animais:
        print(f"- {compatibilidade}") 
    print("="*100 + "\n")

while True:
    print('\nEscolha uma opção:')
    print('1. Adicionar animal')
    print('2. Visualizar animais')
    print('3. Editar animal')
    print('4. Excluir animal')
    print('5. Registrar cuidado')
    print('6. Visualizar cuidados')
    print('7. Editar cuidado')
    print('8. Excluir cuidado')
    print('9. Sugestões personalizadas')
    print('0. Sair')

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
        adicionar_cuidado()
    elif opcao == '6':
        visualizar_cuidados()
    elif opcao == '7':
        editar_cuidado()
    elif opcao == '8':
        excluir_cuidado()
    elif opcao == '9':
        menu_sugestoes_personalizadas(animais)
    elif opcao == '0':
        print('Saindo do programa. Até a próxima!')
        break
    else:
        print('Opção inválida. Tente novamente.')
