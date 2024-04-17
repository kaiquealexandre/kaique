print("Programa de tabuada.")

numero_fornecido = int(input("Digite um número inteiro:"))
multiplicador = 1
while(multiplicador <= 10):
    resultado = numero_fornecido * multiplicador
    print(numero_fornecido, "X", multiplicador, "=", resultado)
    multiplicador = multiplicador + 1
