# Leia seis números inteiros. Ao final, mostre a soma de todos os números e quantos deles são maiores que zero.

# Use um acumulador para a soma e um contador para os positivos. O zero participa da soma, mas não deve ser contado como positivo.

# Teste com números positivos, negativos e zero na mesma execução.
total = 0
numberAboveZer = 0
for number in range(1,7):
    number = int(input("Digite um numero:"))
    total += number
    if number > 0:
        numberAboveZer += 1

print(f"SOMA = {total}")
print(f"NUMEROS MAIORES QUE ZERO = {numberAboveZer}")
    
    

