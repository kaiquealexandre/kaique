print("programa para calcular o imc")
sexo = str(input("digite M para Mulher e H para Homem:"))
peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))

imc = peso / (altura * altura)

if(sexo == "M"):
    if(imc <= 19.1):
        print("você esta abaixo do peso")
    elif(imc <= 25.8):
        print("você esta no peso ideal")
    else:
        print("você é obeso")
elif(sexo == "H"):
    if(imc <= 20.7):
        print("você esta abaixo do peso")
    elif(imc <= 26.4):
        print("você esta no peso ideal")
    else:
        print("você é obeso")
