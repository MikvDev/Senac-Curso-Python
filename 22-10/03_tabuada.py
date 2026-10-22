# Solicite um número inteiro e apresente sua tabuada de multiplicação de 1 até 10 utilizando while.

number = int(input("Digite um numero:"))
i = 0
while i <= 10:
    print(f" {number} x {i} = {number * i}")
    i += 1