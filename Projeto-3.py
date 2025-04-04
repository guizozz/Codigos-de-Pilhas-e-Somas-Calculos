# Inicializa a pilha vazia
pilha = []

# Leitura dos dados de 10 pessoas
for i in range(10):
    print(f"\nDigite os dados da {i+1}ª pessoa:")
    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))
    pilha.append((idade, altura))  # Adiciona um tupla (idade, altura) à pilha

# Imprime o conteúdo completo da pilha
print("\nConteúdo completo da pilha:")
for pessoa in pilha:
    print(f"Idade: {pessoa[0]}, Altura: {pessoa[1]:.2f} m")

# Desempilha e mostra informações de pessoas com idade > 18
print("\nInformações das pessoas com idade maior que 18 anos:")
while pilha:
    idade, altura = pilha.pop()  # Remove o último elemento da pilha
    if idade > 18:
        print(f"Idade: {idade}, Altura: {altura:.2f} m")
