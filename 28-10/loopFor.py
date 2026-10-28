for numero in range(1 ,6):
    print("Numero de 1 até 5:", numero)

for numero in range(5):
    print("Numeros de 0 até 4:",numero)

for numero in range(2,11,2):
    print("Numeros de 2 em 2:",numero)

for numero in range(10,0, -1):
    print("\nDiminuindo numeros:",numero, end=',')
# sep é antes 
# end é depois 

# Exemplo tabuada

numero = int(input("Digite um numero inteiro:"))

for multiplicador in range(1,11):
    resultado = multiplicador * numero
    print(f'{numero} X {multiplicador} = {resultado}')


# exemplo para exercitar

total = 0

for numero in range(2, 8, 2):
    total += numero
    print(numero, total)

print("Total:", total)

# Aqui o numero a cada incremento cresce + 2, e ele soma com o valor de total:
# 2
# 6
# 12
# 20

# Loop d