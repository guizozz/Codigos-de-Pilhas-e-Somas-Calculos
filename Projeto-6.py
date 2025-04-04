# Inicializa a pilha vazia
pilha = []

# Leitura de 15 números
for i in range(15):
    numero = int(input(f"Digite o {i+1}º número: "))
    # Verifica se o número é par
    if numero % 2 == 0:
        pilha.append(numero)  # Adiciona o número à pilha se for par

# Exibe a quantidade de elementos na pilha
print(f"\nQuantidade de números pares na pilha: {len(pilha)}")

# Desempilha e exibe todos os números pares
print("\nNúmeros pares desempilhados:")
while pilha:
    print(pilha.pop())  # Remove e exibe o último elemento da pilha
