maca = 2,40
compra = int(input("Quantas maçãs você vai comprar?"))

if(compra < 12):
    maca = 2,80
else:
    maca = 2,40

valor = compra * maca

print("O preço é: {}" .format(valor))