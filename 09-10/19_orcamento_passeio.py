# Uma turma com 20 alunos fará um passeio. O ônibus custa R$ 600.00 para toda a turma. Cada ingresso custa R$ 15.00 e cada lanche custa R$ 10.00 por aluno.

# Crie variáveis para os dados e calcule, em variáveis separadas:

# o custo de todos os ingressos;
# o custo de todos os lanches;
# o custo total do passeio, incluindo o ônibus uma única vez;
# o valor que cada aluno deverá pagar, dividindo o custo total igualmente.
# Mostre um relatório com a quantidade de alunos e todos os custos. Depois altere a quantidade de alunos para 25 e execute novamente sem modificar as fórmulas.

# Para pensar: por que o custo total aumenta, mas o valor por aluno diminui?

alunos = 15
valor_onibus = 600.00
valor_total_ingressos = alunos * 15
valor_total_lanches = alunos * 10
valor_total_viagem = valor_onibus + valor_total_ingressos + valor_total_lanches

print("Total alunos:", alunos)
print("Total para lanches: ", valor_total_lanches)
print("Total para onibus:", valor_onibus)
print("Total para ingressos:", valor_total_ingressos)
print("Total para a viagem:", valor_total_viagem)


valor_pagar_aluno = valor_total_viagem / alunos
print("O Valor total que cada aluno devera pagar sera de: ", valor_pagar_aluno)
print("\n==============================\n")

alunos = 25

print("Total alunos:", alunos)
print("Total para lanches: ", valor_total_lanches)
print("Total para onibus:", valor_onibus)
print("Total para ingressos:", valor_total_ingressos)
print("Total para a viagem:", valor_total_viagem)

valor_pagar_aluno = valor_total_viagem / alunos
print("O Valor total que cada aluno devera pagar sera de: ", valor_pagar_aluno)