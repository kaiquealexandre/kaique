print("Programa para verificação da Glicose")
def classificar_glicose(glicose):
    if glicose <= 100:
        return "Normal"
    elif glicose <= 140:
        return "High"
    else:
        return "Diabetes"

def main():
    try:
        glicose = int(input("Digite a quantidade de glicose no sangue: "))
        classificacao = classificar_glicose(glicose)
        print("Classificação da glicose:", classificacao)
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()