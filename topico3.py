from datetime import datetime

def calcular_dias_restantes(data_prevista):
    hoje = datetime.today()
    data = datetime.strptime(data_prevista, '%d/%m/%Y')
    diferenca = data- hoje
    return diferenca.days

def mostrar_contagem_regressiva(animal, cuidados):
    print(f'\n   Próximas tarefas para {animal}:')
    encontrou = False
    for cuidado in cuidados:
        if cuidado['animal'].lower() == animal.lower():
            encontrou = True
            dias_restantes = calcular_dias_restantes(cuidado['data'])
            if dias_restantes > 0:
                print(f"   - {cuidado['tipo']} em {cuidado['data']} (Faltam {dias_restantes} dias)\n")
            if dias_restantes < 0:
                print(f"   - {cuidado['tipo']} está atrasado! Por favor, realize o mais rápido possível.\n")
            elif dias_restantes == 0:
                print(f"   - {cuidado['tipo']} está previsto para hoje!\n")
    if not encontrou:
        print ('Nenhuma tarefa encontrada para este animal.\n')