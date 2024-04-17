def fat(f):
    print("Programa para calcular o fatorial.")
    fatorial = 1
    cont = f
    while(cont > 1):
        fatorial = fatorial * cont
        cont -= 1
    print("O fatorial de {} é: {}".format(f, fatorial))

def cubo(n):
    print("Programa para calcular o cubo de um número.")
    cubo = n * n * n
    print("O cubo de {} é: {}".format(n, cubo))

print("Programa para calcular o Fatorial e o Cubo")
numero = int(input("Digite um número:"))
op = int(input("Digite '1' para fatorial, e '2' para cubo:"))
if(op == 1):
    fat(numero)
if(op == 2):
    cubo(numero)