print("Programa para ordenar números")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

a = n1 < n2 < n3
b = n1 < n3 < n2
c = n2 < n1 < n3
d = n2 < n3 < n1
e = n3 < n1 < n2
f = n3 < n2 < n1

if a:
    print('{}, {}, {}'.format(n1, n2, n3))
elif b:
    print('{}, {}, {}'.format(n1, n3, n2))
elif c:
    print('{}, {}, {}'.format(n2, n1, n3))
elif d:
    print('{}, {}, {}'.format(n2, n3, n1))
elif e:
    print('{}, {}, {}'.format(n3, n1, n2))
else:
    print('{}, {}, {}'.format(n3, n2, n1))