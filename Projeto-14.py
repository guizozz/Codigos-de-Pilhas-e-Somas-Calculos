from collections import deque

# Função para calcular a média e verificar a aprovação
def calcular_media_e_aprovacao(p1, p2, p3, frequencia):
    media = (p1 + p2 + p3) / 3
    aprovado = media >= 7 and frequencia > 75
    return media, aprovado

# Inicializa a fila
fila = deque()

# Leitura dos dados dos 15 alunos
for i in range(15):
    print(f"\nAluno {i+1}:")
    matricula = input("Matrícula: ")
    p1, p2, p3 = float(input("Nota P1: ")), float(input("Nota P2: ")), float(input("Nota P3: "))
    frequencia = float(input("Frequência: "))
    
    # Calcula a média e aprovação
    media, aprovado = calcular_media_e_aprovacao(p1, p2, p3, frequencia)
    
    # Armazena os dados do aluno na fila
    fila.append({'matricula': matricula, 'notas': [p1, p2, p3], 'frequencia': frequencia, 'media': media, 'aprovado': aprovado})

# Funções para operações da fila
def buscar_aluno(matricula):
    for i, aluno in enumerate(fila):
        if aluno['matricula'] == matricula:
            return i + 1  # Retorna posição na fila (começando de 1)
    return -1  # Aluno não encontrado

def imprimir_resultados(filtro=None):
    for aluno in fila:
        if filtro is None or filtro(aluno):
            print(f"Matricula: {aluno['matricula']}, Notas: {aluno['notas']}, Frequência: {aluno['frequencia']}, Média: {aluno['media']}")

# Menu interativo
while True:
    print("\nMenu:")
    print("1. Contar alunos")
    print("2. Imprimir fila")
    print("3. Buscar aluno por matrícula")
    print("4. Imprimir aluno por posição")
    print("5. Imprimir aprovados")
    print("6. Imprimir reprovados")
    print("7. Reprovados por frequência")
    print("8. Reprovados por nota")
    print("9. Verificar aprovação por matrícula")
    print("10. Sair")
    
    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        print(f"Quantidade de alunos na fila: {len(fila)}")
    elif escolha == 2:
        imprimir_resultados()
    elif escolha == 3:
        matricula = input("Digite a matrícula: ")
        posicao = buscar_aluno(matricula)
        if posicao != -1:
            print(f"Aluno na posição {posicao}")
        else:
            print("Aluno não encontrado")
    elif escolha == 4:
        pos = int(input("Digite a posição (1-15): "))
        if 1 <= pos <= len(fila):
            aluno = fila[pos - 1]
            print(f"Matricula: {aluno['matricula']}, Notas: {aluno['notas']}, Frequência: {aluno['frequencia']}, Média: {aluno['media']}")
        else:
            print("Posição inválida")
    elif escolha == 5:
        imprimir_resultados(lambda aluno: aluno['aprovado'])
    elif escolha == 6:
        imprimir_resultados(lambda aluno: not aluno['aprovado'])
    elif escolha == 7:
        imprimir_resultados(lambda aluno: aluno['frequencia'] < 75)
    elif escolha == 8:
        imprimir_resultados(lambda aluno: aluno['media'] < 7)
    elif escolha == 9:
        matricula = input("Digite a matrícula: ")
        posicao = buscar_aluno(matricula)
        if posicao != -1:
            aluno = fila[posicao - 1]
            status = "Aprovado" if aluno['aprovado'] else "Reprovado"
            print(f"Aluno {matricula} está {status}")
        else:
            print("Aluno não encontrado")
    elif escolha == 10:
        break
    else:
        print("Opção inválida")
