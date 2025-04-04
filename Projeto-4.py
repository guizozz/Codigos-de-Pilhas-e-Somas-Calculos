# Inicializa a soma dos números
soma = 0

# Lê 5 números inteiros do usuário
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    soma += numero  # Soma os números

# Calcula a média
media = soma / 5

# Exibe a média
print(f"\nA média dos números digitados é: {media:.2f}")
