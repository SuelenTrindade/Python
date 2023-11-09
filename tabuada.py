numero = None
while numero is None or numero < 0 or numero > 10:
    try:
        numero = int(input())
        if numero < 0 or numero > 10:
            print("VALOR INVÁLIDO")
    except ValueError:
        print()
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero}x{i}={resultado}")