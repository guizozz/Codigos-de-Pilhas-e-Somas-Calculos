# Inicializa a pilha vazia
pilha = []

# Leitura de altura e idade de 10 jogadores
for i in range(10):
    print(f"\nCadastro do {i+1}º jogador:")
    altura = float(input("Digite a altura do jogador (em metros): "))
    idade = int(input("Digite a idade do jogador: "))
    
    # Adiciona as informações na pilha
    pilha.append({"altura": altura, "idade": idade})

# Desempilhando e verificando a altura dos jogadores
print("\nAnálise dos jogadores para o campeonato:")
while pilha:
    jogador = pilha.pop()  # Desempilha o último jogador
    
    if jogador["altura"] > 1.90:
        print(f"Jogador com altura {jogador['altura']}m e idade {jogador['idade']} anos irá participar do campeonato.")
    else:
        print("Jogador não irá participar do campeonato.")
