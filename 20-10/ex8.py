# Desafiador
# Desenvolva um programa que receba três números representando os lados de um possível triângulo.

# Para formar um triângulo, os três lados devem ser positivos e satisfazer:

# a+b>c E a+c>b E b+c>a
# Caso seja possível formar um triângulo, classifique-o:

# Tipo	Condição
# Equilátero	Três lados iguais
# Isósceles	Exatamente dois lados iguais
# Escaleno	Três lados diferentes
# Se os valores não formarem um triângulo, mostre Triângulo inválido.

# Desafio: Realize primeiro a validação e somente depois a classificação.

a = float(input("Digite o valor do lado do tringulo:")) # a
b = float(input("Digite o valor do lado do tringulo:")) # b
c = float(input("Digite o valor do lado do tringulo:")) # c

if a > 0 and b > 0 and c > 0 and (a + b > c and a + c > b and  b + c > a):
    if a == b and b == c:
        print("Equilátero - Três lados iguais")
    elif (a == b or b == c) or a == c:
        print("Isósceles - dois lados iguais ")
    else:
        print("Este triangulo é escaleno!")
   
else:
    print("Triângulo inválido.")