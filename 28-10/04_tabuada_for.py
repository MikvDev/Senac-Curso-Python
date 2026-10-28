# Leia um inteiro e apresente sua tabuada de multiplicação de 1 até 10, utilizando for. Cada linha deve mostrar os dois fatores e o resultado.


numero = int(input("Digite um numero inteiro:"))

for multiplicador in range(1,11):
    resultado = multiplicador * numero
    print(f'{numero} X {multiplicador} = {resultado}')