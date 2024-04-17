print("Programa que calcula o ano bissexto")

try:
    ano = int(input("Digite o ano:"))
    if(ano%400 == 0 or ano%4 == 0 and ano%100 != 0):
        print("{} é ano bissexto.".format(ano))
    else:
        print("{} não é bissexto.".format(ano))
except Exception as e:
    print("Ocorreu o seguinte erro {}, seu programa será finalizado.".format(type(e)))
print("Fim de programa.")