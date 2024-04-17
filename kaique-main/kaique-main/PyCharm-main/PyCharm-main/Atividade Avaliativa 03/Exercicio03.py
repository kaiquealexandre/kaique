print("Programa que calcula o IMC (Índice de massa corporal).")

genero = input("Digite 'M' para Mulheres ou 'H' para Homens: ").upper()
peso = float(input("Digite o peso em Kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if genero == "M":
    if imc < 19.1:
        print("Abaixo do peso")
    elif 19.1 <= imc <= 25.8:
        print("Peso ideal")
    else:
        print("Obeso")
elif genero == 'H':
    if imc < 20.7:
        print("Abaixo do peso")
    elif 20.7 <= imc <= 26.4:
        print("Peso ideal")
    else:
        print("Obeso")
else:
    print("Sexo não reconhecido. Por favor, digite 'M' para mulher ou 'H' para homem.")