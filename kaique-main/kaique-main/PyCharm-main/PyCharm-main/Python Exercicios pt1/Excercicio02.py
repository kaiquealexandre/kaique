def calcular_volume(lado):
    volume = lado ** 3
    return volume
def main():
    lado = float(input("Digite o comprimento do lado da caixa de água (em metros): "))
    volume = calcular_volume(lado)
    print("O volume da caixa d'água é de", volume, "metros cúbicos.")

if __name__ == "__main__":
    main()