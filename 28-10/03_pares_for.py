# Leia um inteiro positivo e mostre os números pares de 2 até o limite, incluindo-o quando ele for par. Utilize o passo de range().

# Se o limite for 1, informe que não há pares no intervalo. Para valores menores ou iguais a zero, informe que o limite é inválido.

# Teste com 1, 2, 9 e 10.

numberLimit = int(input("Digite um numero:"))
if numberLimit >= 0:
    for number in range(1,numberLimit,2):
        print(number)
else:
    print("Valor inválido!")