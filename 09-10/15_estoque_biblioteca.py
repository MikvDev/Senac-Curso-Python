# A biblioteca começa o dia com 40 livros disponíveis. Nesta ordem:

# recebe 12 livros novos;
# empresta 9 livros;
# recebe a devolução de 4 livros;
# empresta mais 6 livros.
# Crie uma variável livros_disponiveis e atualize essa mesma variável após cada acontecimento. Mostre a quantidade inicial e a quantidade após cada atualização, identificando a etapa.

# Antes de executar, anote em comentários suas previsões para cada etapa. Compare com o resultado do programa.

# Variaveis 
livros_disponiveis = 12


# livrosEmprestados = livros - 9
# livrosDevolvidos = livrosEmprestados + 4
# livrosEmprestados = livrosDevolvidos  - 6




print("============= Biblioteca ==============")
# O resultado será 3, pois emprestamos 9 livros.
print(f"Livros emprestados - 9 - | disponiveis:  {livros_disponiveis - 9}")
# o resultado será 7, pois foram devolvidos 4.
print(f"Livros devolvidos - 4 - | disponiveis: {livros_disponiveis + 4}")
# o resultado será 1, pois foram devolvidos 6.
print(f"Livros devolvidos - 6 - | disponiveis: {livros_disponiveis - 6}")
