print("Programa para verificar maior e menor valor")

maior_valor = 0
menor_valor = 0

while True:
    numero = int(input("Digite um número:"))
    if(numero == 0):
        break
    if(maior_valor == 0 and menor_valor == 0):
        maior_valor = numero
        menor_valor = numero

    if(numero > maior_valor):
        maior_valor = numero
    if(numero < menor_valor):
        menor_valor = numero
print("O maior valor é {}, e o menor valor é {}" .format(maior_valor, menor_valor))