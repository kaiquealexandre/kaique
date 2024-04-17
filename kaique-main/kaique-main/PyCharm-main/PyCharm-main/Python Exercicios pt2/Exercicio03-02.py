print("Programa para calcular juros simples.")

capital = float(input("Entre com o capital:"))
taxa = float(input("Entre com as taxas:"))
tempo =  int(input("Entre com o número de meses:"))

j = (capital * taxa * tempo) / 100
print("O juro cobrado é: ", j)