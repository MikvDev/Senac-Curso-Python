# Leia dois números decimais. Mostre um menu com as opções 1 para somar, 2 para subtrair, 3 para multiplicar e 4 para dividir. Leia a opção como texto.

# Execute somente a operação escolhida. Se a opção não existir, mostre Opção inválida. Na divisão, verifique se o segundo número é zero antes de calcular; nesse caso, mostre Não é possível dividir por zero.

number_one = float(input("Digite um numero:"))
number_two = float(input("Digite um numero:"))

print("============ Menu ===============" \
"n1 - Somar" \
"n2 - Subtrair" \
"n3 - Multiplicar" \
"n4 - Dividir" )

if number_one == 1:
    print("Soma:", number_one + number_two)
elif number_one == 2:
    print("Subtração:", number_one - number_two)
elif number_one == 3:
    print("Multiplicação:", number_one * number_two)
elif number_one == 4:
    if number_two != 0:
        print("Divisão:", number_one / number_two)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida.")