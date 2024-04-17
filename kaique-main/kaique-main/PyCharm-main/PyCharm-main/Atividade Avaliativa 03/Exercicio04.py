print("Programa que calcula a distribuição de gêneros na população.")

homens = 0
mulheres = 0

for _ in range(15):
    sexo = input("Digite o sexo da pessoa (H para homem, M para mulher): ").upper()
    if sexo == 'H':
        homens += 1
    elif sexo == 'M':
        mulheres += 1
    else:
        print("Entrada inválida. Por favor, digite H para homem ou M para mulher.")

print("Quantidade de Homens:", homens)
print("Quantidade de Mulheres:", mulheres)
