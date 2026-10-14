# Um personagem possui inicialmente:

# 200 pontos de vida

# Durante uma batalha:

# recebe 45 de dano
# recebe 30 de dano
# recupera 20 pontos de vida

# Crie uma variável vida e atualize seu valor depois de cada acontecimento.

# Mostre somente a quantidade final de vida.

life_points = 200

life_points -= 45
life_points -= 30
life_points += 20

print("O heroi está com", life_points, "de vida.")