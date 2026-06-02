def menu_sugestoes_personalizadas(animais):
    nome_busca = input('Digite o nome do animal para buscar sugestões personalizadas: ')
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
    if "agitado" in comportamento or "ativo" in comportamento or "brincalhão" in comportamento:
        sugestoes_adotante.append("Casas com quintal grande ou tutores que praticam corridas/caminhadas.")
        compatibilidade_com_outros_animais.append("Excelente para conviver com crianças ativas.")
    elif "calmo" in comportamento or "medroso" in comportamento or "tranquilo" in comportamento:
        sugestoes_adotante.append("Ambientes silenciosos e sem muita movimentação ou barulho excessivo.")
        compatibilidade_com_outros_animais.append("Pode se assustar com crianças muito pequenas; prefere ambientes tranquilos.")

    print("\n" + "="*50)
    print(f"Sugestões personalizadas para o animal '{animal_encontrado['nome']}':")
    print("="*50)

    print("\nSugestões de adotantes ideais:")
    for sugestao in sugestoes_adotante:
        print(f"- {sugestao}")

    print("\nCuidados especiais necessários:")
    for cuidado in cuidados_especiais:
        print(f"- {cuidado}")

    print("\nCompatibilidade com outros animais e crianças:")
    for compatibilidade in compatibilidade_com_outros_animais:
        print(f"- {compatibilidade}")   
    print("="*50 + "\n")