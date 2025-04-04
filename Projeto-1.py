# Inicializa o vetor
numeros = []

# Lê 10 números inteiros do usuário
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Calcula a soma dos números no vetor
soma = sum(numeros)

# Exibe a soma
print("\nA soma de todos os números é:", soma)
