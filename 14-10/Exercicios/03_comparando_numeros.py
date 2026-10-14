# Leia dois números inteiros. Informe se o primeiro é maior, se o segundo é maior ou se os dois são iguais. Use uma cadeia if / elif / else.

number_one = int(input("Digite um numero:"))
number_two = int(input("Digite outro numero:"))

if number_one > number_two:
    print("Numero um é maior que numero dois.")
else:
    print("Numero dois é maior que numero um.")