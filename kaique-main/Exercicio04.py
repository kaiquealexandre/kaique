sequencia = 1
homem = 0
mulher = 0
while(sequencia <= 15):
    sexo = input("digite M para Mulher e H para Homem, {}° pessoa:" .format(sequencia))
    if(sexo.upper() == "H"):
        homem = homem + 1
    elif(sexo.upper() == "M"):
        mulher = mulher + 1
    else:
        print("ocorreu um erro digite novamente")
        sequencia -= 1
    sequencia += 1