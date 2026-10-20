# Um jogo de RPG classifica seus aventureiros de acordo com o nível alcançado.

# Solicite o nome e o nível de um personagem e determine sua classificação:

# Nível	Classificação
# 1 a 5	Aprendiz
# 6 a 15	Guerreiro
# 16 a 30	Veterano
# 31 ou superior	Lendário

# Requisitos:

# Não permita níveis menores que 1.
# Mostre o nome do personagem e sua classificação.
# Utilize if, elif e else.


nivel = int(input("Digite o nível do personagem:"))
if nivel < 1:
    print("Valor invalido! Níveis menores que 1 não são permitidos")    
elif nivel >= 1 and nivel <= 5:
    print("O personagem é um Aprendiz!")
elif nivel >= 6 and nivel <= 15:
    print("O personagem é um Guerreiro!")
elif nivel >= 16 and nivel <= 30:
    print("O personagem é um Veterano!")
else:
    print("O personagem é um Lendário!")