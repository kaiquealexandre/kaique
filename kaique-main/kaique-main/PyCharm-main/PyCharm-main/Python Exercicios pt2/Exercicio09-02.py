print("Calculador Python")

while True:
    try:
        numero1 = float(input("Digite o primeiro número:"))
        numero2 = float(input("Digite o segundo número:"))
        operacao = input("Digite a operação desejada:")

        if(operacao == "+"):
            total = numero1 + numero2
        elif(operacao == "*"):
            total = numero1 * numero2
        elif(operacao == "/"):
            total = numero1/numero2
        elif(operacao == "-"):
            total = numero1 - numero2
        elif (operacao.upper() == "S"):
            break
        else:
            print("Valor Inválido.")
            continue
        print("A operação escolhida foi {} e o resultado é {}".format(operacao, total))
    except:
       print("Você digitou um valor inválido.")
print("Fim de programa.")