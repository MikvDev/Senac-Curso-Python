# Leia duas notas de mesmo peso. Se alguma nota estiver fora da faixa de 0 a 10, mostre Nota inválida e não calcule a média. Caso ambas sejam válidas, calcule e mostre a média e a situação:

# média a partir de 7: aprovado;
# média a partir de 5 e abaixo de 7: recuperação;
# média abaixo de 5: reprovado.

grade_one = float(input("Digite sua nota:"))
if grade_one > 10 and grade_one < 0:
    print("Valor invalido")

grade_two = float(input("Digite sua nota:"))
if grade_two > 10 and grade_two < 0:
    print("Valor invalido")

grade_avarege = (grade_one + grade_two) / 2

if grade_avarege >= 7:
    print("Aprovado")
elif grade_avarege >= 5:
    print("Recuperação")
else:
    print("Reprovado")
