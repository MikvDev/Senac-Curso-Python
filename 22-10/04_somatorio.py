# Solicite cinco números inteiros e apresente a soma de todos eles.

# Utilize um contador para controlar as repetições e um acumulador para guardar a soma.



i = 0
sum = 0
while i <= 5:
    grade = float(input(f"Digite o valor - {i}: "))
    sum += grade
    i+=1



print(sum)