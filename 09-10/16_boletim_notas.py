# Um aluno recebeu as notas 7.5, 8.0 e 9.5 em três atividades de mesmo peso.

# Guarde o nome do aluno e cada nota em variáveis separadas.
# Calcule a soma das notas em uma variável soma_notas.
# Calcule a média dividindo a soma pela quantidade de atividades.
# Mostre o nome, as três notas e a média.
# Troque apenas a segunda nota por 6.5 no código e execute novamente.
# O programa deve recalcular a média a partir das variáveis. Não escreva a média pronta no código. Não é necessário informar aprovação ou reprovação.

# Variaveis
nomeAluno = "Miguel Vargas Ferreira"
nota1 = 7.5 
nota2 = 8.0
nota3 = 9.5
soma_notas = (nota1 + nota2 + nota3) / 3

print("======================================")
print(f"Nome:  {nomeAluno}")
print(f"Nota 1:  {nota1}")
print(f"Nota 2:  {nota2}")
print(f"Nota 3:  {nota3}")
print(f"Media das notas: {soma_notas:.2f}")
print("=====================================")
nota2 = 6.5
soma_notas = (nota1 + nota2 + nota3) / 3

print(f"Nota 2 - alterada - 6.5")
print(f"Nova media: {soma_notas:.2f}")