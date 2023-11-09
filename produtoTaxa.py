# Função para atualizar o preço com aumento de 10%
def atualiza_preco(valor):
    novo_valor = valor * 1.10  # Aumenta em 10%
    return novo_valor

# Função para calcular a taxa de 2.5%
def taxa(valor):
    taxa = valor * 0.025  # 2.5% é igual a 0.025 como decimal
    return taxa

# Função principal
def main():
    # Solicita que o usuário insira o valor do produto
    valor_produto = float(input("Digite o valor do produto: "))

    # Chama a função para atualizar o preço
    valor_atualizado = atualiza_preco(valor_produto)

    # Chama a função para calcular a taxa
    valor_da_taxa = taxa(valor_atualizado)

    # Imprime os valores com duas casas decimais
    print(f"Valor atualizado: R${valor_atualizado:.2f}")
    print(f"Valor da taxa: R${valor_da_taxa:.2f}")

# Chama a função principal
main()
