from collections import deque

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Inicializa a fila
fila = deque()

# Leitura dos dados de 5 pessoas
for i in range(5):
    print(f"\nPessoa {i+1}:")
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))
    
    # Calcula o IMC
    imc = calcular_imc(peso, altura)
    
    # Armazena os dados e IMC na fila
    fila.append((peso, altura, imc))

# Processa e exibe os resultados para cada pessoa
print("\nResultados:")
while fila:
    peso, altura, imc = fila.popleft()  # Remove os dados da fila

    # Exibe a mensagem conforme o IMC
    if 18.5 <= imc <= 25:
        print(f"IMC: {imc:.2f} - Peso Ideal")
    elif imc > 25:
        print(f"IMC: {imc:.2f} - Você está acima do peso ideal!")
    else:
        print(f"IMC: {imc:.2f} - Você está abaixo do peso ideal")
