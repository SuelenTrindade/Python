def entrada_carro():
    modelos = []
    print()
    for i in range(4):
        modelo = input()
        modelos.append(modelo)
    return modelos
def entrada_consumo():
    consumos = []
    print()
    for i in range(4):
        consumo = int(input(""))
        consumos.append(consumo)
    return consumos
def economico(modelos, consumos):
    indice_menor_consumo = consumos.index(min(consumos))
    modelo_menor_consumo = modelos[indice_menor_consumo]
    return modelo_menor_consumo
def main():
    modelos = entrada_carro()
    consumos = entrada_consumo()
    
    modelo_mais_economico = economico(modelos, consumos)
    
    print(f"{modelo_mais_economico}")
main()
