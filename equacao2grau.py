from math import sqrt

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

delta = (b**2 - 4*a*c)

if delta < 0:
    print("Delta negativo")
else:
    raiz_delta = sqrt(delta)
    x1 = (-b + raiz_delta)/(2*a)
    x2 = (-b - raiz_delta)/(2*a)

    print("As raizes são ", int(x1)," e ", int(x2))