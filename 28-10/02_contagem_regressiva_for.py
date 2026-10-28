# Leia um inteiro maior ou igual a zero. Mostre a contagem desse número até zero e, ao final, Lançamento realizado!. Para uma entrada negativa, apresente uma mensagem de valor inválido e não realize o lançamento.

# Teste com 3, 0 e -1.

number = int(input("Digite um numero:"))
for decreaseNumber in range(number,-1,-1):
    print(decreaseNumber)

print("Lançamento realizado!")