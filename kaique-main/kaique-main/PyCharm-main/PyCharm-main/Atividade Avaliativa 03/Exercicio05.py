print("Programa que verifica a classificação de notas de alunos.")

e = d = c = b = a = 0

for _ in range(15):
    nota_final = float(input("Digite a nota final do aluno: "))

    if 0 <= nota_final < 3:
        e += 1
    elif 3 <= nota_final < 5:
        d += 1
    elif 5 <= nota_final < 7:
        c += 1
    elif 7 <= nota_final < 9:
        b += 1
    else:
        a += 1

print("Quantidade de alunos na classe E:", e)
print("Quantidade de alunos na classe D:", d)
print("Quantidade de alunos na classe C:", c)
print("Quantidade de alunos na classe B:", b)
print("Quantidade de alunos na classe A:", a)
