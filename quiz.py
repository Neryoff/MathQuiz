import random
import math
import time
import os

ARQUIVO_HISTORICO = "historico_resultados.txt"

def carregar_historico():
    if not os.path.exists(ARQUIVO_HISTORICO):
        return []
    with open(ARQUIVO_HISTORICO, "r") as file:
        linhas = file.readlines()
        return [linha.strip() for linha in linhas]

def salvar_resultado(nome, acertos, erros, percentual, tempo, dificuldade, operacoes):
    with open(ARQUIVO_HISTORICO, "a") as file:
        file.write(f"{nome} - {acertos} acertos, {erros} erros - {percentual:.2f}% - Tempo: {tempo:.2f}s - Dificuldade: {dificuldade} - Op: {', '.join(operacoes)}\n")

def mostrar_resultados():
    os.system('cls' if os.name == 'nt' else 'clear')
    historico = carregar_historico()
    if not historico:
        print("\nNenhum jogo jogado ainda.")
    else:
        print("\n📈 Histórico de Resultados:")
        for i, linha in enumerate(historico):
            print(f"Partida {i + 1}: {linha}")

def escolher_dificuldade():
    print("\nEscolha a dificuldade:")
    print("1. Fácil")
    print("2. Médio")
    print("3. Difícil")
    while True:
        escolha = input("Opção: ")
        if escolha in ['1', '2', '3']:
            return {'1': 'fácil', '2': 'médio', '3': 'difícil'}[escolha]
        else:
            print("Opção inválida. Tente novamente.")

def escolher_operacoes():
    todas_operacoes = {
        '+': 'Adição',
        '-': 'Subtração',
        '*': 'Multiplicação',
        '/': 'Divisão',
        '**': 'Potência',
        '//': 'Divisão inteira',
        '%': 'Resto',
        'raiz': 'Raiz quadrada',
        'abs': 'Módulo'
    }

    print("\nEscolha as operações que deseja praticar (digite os números separados por vírgula):")
    for i, (op, nome) in enumerate(todas_operacoes.items()):
        print(f"{i + 1}. {nome} ({op})")

    while True:
        escolha = input("Ex: 1,2,5: ")
        try:
            indices = [int(i.strip()) for i in escolha.split(',')]
            chaves = list(todas_operacoes.keys())
            selecionadas = [chaves[i - 1] for i in indices if 0 < i <= len(chaves)]
            if selecionadas:
                return selecionadas
        except:
            pass
        print("Escolha inválida. Tente novamente.")

def gerar_pergunta(dificuldade, operacoes):
    op = random.choice(operacoes)

    if dificuldade == 'fácil':
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    elif dificuldade == 'médio':
        a = random.randint(10, 50)
        b = random.randint(5, 30)
    else:
        a = random.randint(-100, 100)
        b = random.randint(1, 50)

    if op == '+':
        return f"Quanto é {a} + {b}? ", a + b
    elif op == '-':
        return f"Quanto é {a} - {b}? ", a - b
    elif op == '*':
        return f"Quanto é {a} * {b}? ", a * b
    elif op == '/':
        a = a * b
        return f"Quanto é {a} / {b}? ", round(a / b, 2)
    elif op == '**':
        b = b % 4 + 2
        return f"Quanto é {a} elevado a {b}? ", a ** b
    elif op == '//':
        return f"Qual é a divisão inteira de {a} por {b}? ", a // b
    elif op == '%':
        return f"Qual o resto da divisão de {a} por {b}? ", a % b
    elif op == 'raiz':
        a = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
        return f"Qual é a raiz quadrada de {a}? ", round(math.sqrt(a), 2)
    elif op == 'abs':
        a = random.randint(-100, 100)
        return f"Qual é o módulo (valor absoluto) de {a}? ", abs(a)

def iniciar_quiz():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎯 Iniciando o Quiz de Matemática Avançado!\n")

    nome = input("Digite seu nome: ").strip()
    while not nome:
        print("Nome não pode ser vazio.")
        nome = input("Digite seu nome: ").strip()

    dificuldade = escolher_dificuldade()
    operacoes = escolher_operacoes()

    num_perguntas = {'fácil': 5, 'médio': 10, 'difícil': 15}[dificuldade]

    acertos = 0
    erros = 0

    tempo_inicio = time.time()

    for i in range(num_perguntas):
        print(f"\nPergunta {i + 1}/{num_perguntas}")
        pergunta, resposta_correta = gerar_pergunta(dificuldade, operacoes)
        try:
            resposta_usuario = float(input(pergunta))
        except ValueError:
            print("❌ Resposta inválida. Contando como erro.")
            erros += 1
            continue

        if abs(resposta_usuario - resposta_correta) < 0.01:
            print("✅ Correto!")
            acertos += 1
        else:
            print(f"❌ Errado! A resposta correta era {resposta_correta}")
            erros += 1

    tempo_fim = time.time()
    duracao = tempo_fim - tempo_inicio
    percentual = (acertos / num_perguntas) * 100

    print("\n📊 Resultado final:")
    print(f"Nome: {nome}")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")
    print(f"Desempenho: {percentual:.2f}%")
    print(f"Tempo total: {duracao:.2f} segundos")

    salvar_resultado(nome, acertos, erros, percentual, duracao, dificuldade, operacoes)

def mostrar_menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Iniciar quiz")
        print("2. Ver histórico de resultados")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            iniciar_quiz()
        elif opcao == '2':
            mostrar_resultados()
        elif opcao == '3':
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    mostrar_menu()

if __name__ == "__main__":
    main()
