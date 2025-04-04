while True:
    # Lê um número inteiro do usuário
    numero = int(input("Digite um número inteiro (ou um número negativo para encerrar): "))
    
    # Verifica se o número é negativo para encerrar o programa
    if numero < 0:
        print("Número negativo informado. Encerrando o programa.")
        break
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é Par.")
    else:
        print(f"O número {numero} é Ímpar.")
