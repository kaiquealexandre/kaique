print("Programa para calcular notas trimestrais.")

trimestre1 = float(input("Digite a nota do primeiro trimestre:"))
trimestre2 = float(input("Digite a nota do segundo trimestre:"))
trimestre3 = float(input("Digite a nota do terceiro trimestre:"))
media = (trimestre1 + trimestre2 + trimestre3)/3
if media < 40:
    print("Aluno reprovado e sua média é: {}".format(media))
elif media >= 40 and media < 60:
    print("Aluno em recuperação e sua média é: {}".format(media))
else:
    print("Aluno aprovado e sua média é {}".format(media))

print("Fim do programa.")