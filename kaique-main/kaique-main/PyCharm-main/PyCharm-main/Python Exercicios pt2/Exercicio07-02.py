print("Programa para calcular imposto de renda.")

salario = float(input("Digite o seu salário:"))
if(salario <= 1903.98):
    print("Você está isento de imposto de renda.")
elif(salario <= 2826.65):
    imposto = (salario * 7.5)/100
elif (salario <= 3751.06):
    imposto = (salario * 15)/ 100
elif(salario <= 4664.68):
    imposto = (salario * 22.5)/100
else:
    imposto = (salario * 27.5)/100

if(salario > 1903.98):
    print("Você deverá pagar R$ {} de impostos".format(imposto))