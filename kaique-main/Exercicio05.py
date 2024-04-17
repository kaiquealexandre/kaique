E = 0
D = 0
C = 0
B = 0
A = 0
contador = 1

while(contador <= 15):
    nota = int(input("digite a nota do {}° aluno:" .format(contador)))
    contador += 1
    if(nota <= 2.9):
        E += 1
    elif (nota <= 4.9):
        D += 1
    elif (nota <= 6.9):
        C += 1
    elif (nota <= 8.9):
        B += 1
    elif (nota <= 10):
        A += 1
    else:
        print("ocorreu um erro, digite novamente")
        contador -= 1
print("{} alunos estão no conceito A, {} no B {} no C {} no D {} no E" .format(A, B, C, D, E))