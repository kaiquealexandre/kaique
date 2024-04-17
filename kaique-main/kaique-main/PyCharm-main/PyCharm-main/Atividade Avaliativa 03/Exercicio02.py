print("Programa que calcula o valor da hora trabalhada.")

salario_base = float(input("Digite o salário base por hora: "))
horas_extras = float(input("Digite o total de horas extras trabalhadas na semana: "))

Salario_hora = salario_base / 40
Salario_extra = horas_extras + Salario_hora *1.5
SalarioTotal = Salario_extra * salario_base

print("O valor da hora trabalhada, considerando as horas extras, é:", SalarioTotal)
