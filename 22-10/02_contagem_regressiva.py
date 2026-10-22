# Solicite um número inteiro positivo e faça uma contagem regressiva até zero.

import time


number = int(input("Digite um numero:"))

while number > 0:
    print(number)
    time.sleep(1)
    number -= 1

print("Cabum!")