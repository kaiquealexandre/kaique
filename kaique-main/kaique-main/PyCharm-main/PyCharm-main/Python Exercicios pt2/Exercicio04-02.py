print("Programa que classifica triângulo.")

ladoA = float(input("Digite o lado A:"))
ladoB = float(input("Digite o lado B:"))
ladoC = float(input("Digite o lado C:"))

if(ladoA > ladoB + ladoC) or (ladoB > ladoA + ladoC) or (ladoC > ladoA + ladoB):
    print("Não é um triângulo.")
else:
    print("É um triângulo.")
    if(ladoA == ladoB and ladoB == ladoC):
        print("Triângulo equilátero.")
    elif(ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
        print("Triângulo isóceles.")
    else:
        print("Triângulo escaleno.")
    