
# Leia um número inteiro positivo e mostre os números de 1 até ele, incluindo o limite. Se a entrada for menor ou igual a zero, mostre uma mensagem de valor inválido.

# Teste com 1, 5 e 0.

numberLimit = int(input("Digite um numero:"))

if numberLimit <= 0:
    print("Valores menor que 0 são inválidos")
else:
    for initialNumber in range(1, numberLimit + 1 ):
        print(initialNumber)