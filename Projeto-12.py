import math

def calcular_area_quadrado(lado):
    return lado ** 2

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

while True:
    # Exibe o menu de opções
    print("\nMenu:")
    print("1. Calcular a área de um quadrado")
    print("2. Calcular a área de um círculo")
    print("3. Calcular a área de um triângulo")
    print("4. Sair")
    
    # Solicita a escolha do usuário
    escolha = int(input("Escolha uma opção (1-4): "))
    
    if escolha == 1:
        # Calcular área do quadrado
        lado = float(input("Digite o valor do lado do quadrado: "))
        area = calcular_area_quadrado(lado)
        print(f"A área do quadrado é: {area:.2f}")
    
    elif escolha == 2:
        # Calcular área do círculo
        raio = float(input("Digite o valor do raio do círculo: "))
        area = calcular_area_circulo(raio)
        print(f"A área do círculo é: {area:.2f}")
    
    elif escolha == 3:
        # Calcular área do triângulo
        base = float(input("Digite o valor da base do triângulo: "))
        altura = float(input("Digite o valor da altura do triângulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"A área do triângulo é: {area:.2f}")
    
    elif escolha == 4:
        # Sair do programa
        print("Saindo do programa. Até logo!")
        break
    
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")
