import math

a = float(input())
b = float(input())
c = float(input())
delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz= (- b + math.sqrt(delta)) / (2 * a)
    print("A única raíz é: ", raiz)
else:
    if delta < 0:
        print("Essa equação não possuí raizes reais")
    else:
        raiz= (- b + math.sqrt(delta)) / (2 * a)
        raiz2= (- b - math.sqrt(delta)) / (2 * a)
        print(raiz)
        print(raiz2)
