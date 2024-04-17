print("Programa para calcular o fatorial.")

numero = int(input("Digite um número:"))
fatorial = 1
cont = numero
while(cont > 1):
    fatorial = fatorial * cont
    cont -= 1
print("O fatorial de {} é: {}".format(numero, fatorial))