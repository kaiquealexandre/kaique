import random
print("*********************")
print("Bem vindo ao jogo de advinhação.")
print("**********************")

numero_secreto = random.randint(1, 50)
total_de_tentativas = 0
rodada = 1
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil , (2) Médio , (3) Difícil")

nivel = int(input("Defina o nível:"))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}" .format( rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 50:"))
    print("Você digitou: ", chute)

    if(chute < 1 or chute > 50):
        print("Digite um número entre 1 e 50:")
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos." .format(pontos))
        break
    else:
        if(maior):
            print("Você errou! Digite um número menor. Seus pontos:" ,pontos)
        elif(menor):
            print("Você errou! Digite um número maior. Seus pontos:" ,pontos)
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("O numéro secreto é: ", numero_secreto)
print("Fim do jogo. Seus pontos:" ,pontos)
print("Deseja jogar novamente?")