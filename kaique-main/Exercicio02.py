def calcular_valor_da_hora(valor_por_hora_normal, percentual_extra):
    return valor_por_hora_normal * (1 + percentual_extra/100)

def main():
    valor_por_hora_normal = float(input("Digite o valor por hora normal: "))
    percentual_extra = 50  # 50% a mais sobre o valor da hora normal

    valor_por_hora_com_extra = calcular_valor_da_hora(valor_por_hora_normal, percentual_extra)

    print("O valor da hora trabalhada, considerando 50% a mais para hora extra, é:", valor_por_hora_com_extra)

if __name__ == "__main__":
    main()