# Inicialize uma variável para armazenar o número
numero = None

# Use um loop para validar a entrada
while numero is None or numero <= 0:
    try:
        numero = int(input("Digite um número inteiro e positivo: "))
        if numero <= 0:
            print("VALOR INVÁLIDO. O número deve ser positivo.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro positivo válido.")

# Inicialize uma lista para armazenar os divisores
divisores = []

# Encontre os divisores do número
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Imprima os divisores separados por espaço
divisores_str = ' '.join(map(str, divisores))
print(f"Divisores de {numero}: {divisores_str}")
