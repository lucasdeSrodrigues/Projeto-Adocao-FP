def animal_destaque():
    if not animais:
        print("Nenhum animal cadastrado.")
        return

    melhor_animal = None
    maior_pontuacao = -1

    for animal in animais:
        pontos = 0

        if animal['saúde'].lower() == 'saudavel':
            pontos += 30

        if animal['idade'] <= 5:
            pontos += 20

        if animal['comportamento'].lower() == 'calmo':
            pontos += 20

        if animal['especie'].lower() == 'cachorro':
            pontos += 10

        if pontos > maior_pontuacao:
            maior_pontuacao = pontos
            melhor_animal = animal

    print("\n" + "="*40)
    print("ANIMAL DESTAQUE DO ABRIGO")
    print("="*40)
    print(f"Nome: {melhor_animal['nome']}")
    print(f"Espécie: {melhor_animal['especie']}")
    print(f"Raça: {melhor_animal['raca']}")
    print(f"Idade: {melhor_animal['idade']} anos")
    print(f"Saúde: {melhor_animal['saúde']}")
    print(f"Pontuação: {maior_pontuacao}")
    print("\nMotivos para destaque:")

    if melhor_animal['saúde'].lower() == 'saudavel':
        print("- Animal saudável")

    if melhor_animal['idade'] <= 5:
        print("- Animal jovem")

    if melhor_animal['comportamento'].lower() == 'calmo':
        print("- Comportamento tranquilo")

    print("="*40)