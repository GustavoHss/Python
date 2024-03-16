numero1 = int(input("Informe o número 1: "))
sinal = input("Informe o operador: ")
numero2 = int(input("Informe o número 2: "))


if sinal == "+":
    op = numero1 + numero2
elif sinal == "-":
    op = numero1 - numero2
elif sinal == "*":
    op = numero1 * numero2
elif sinal == "/":
    op = numero1 / numero2
elif sinal == "%":
    op = numero1 % numero2
elif sinal == "**":
    op = numero1 ** numero2
else:
    print("Sinal inválido")

print(op)