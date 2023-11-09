def entrada_carro():
    carro = []
    for i in range(4):
        carro.append(input("Digite o modelo do carro: "))
    return carro

def entrada_consumo():
    consumo = []
    for i in range(4):
        consumo.append(int(input()))
    return consumo

def economico(carro, consumo):
    menor_consumo = consumo[0]
    modelo_economico = carro[0]
    for i in range(1, len(consumo)):
        if consumo[i] < menor_consumo:
            menor_consumo = consumo[i]
            modelo_economico = carro[i]
    return modelo_economico

def main():
    carro = entrada_carro()
    consumo = entrada_consumo()
    modelo = economico(carro, consumo)
    print(f"{modelo}")

if __name__ == "__main__":
    main()
