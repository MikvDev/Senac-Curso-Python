# Sem utilizar nenhum recurso além do que foi visto na aula, crie um pequeno sistema representando um personagem de RPG.

# O personagem deve possuir:

# nome
# vida
# ouro
# nivel

# Durante a aventura:

# ganha ouro
# recebe dano
# gasta ouro
# recupera vida
# sobe de nível

# Cada acontecimento deve alterar a variável correspondente.

# No final, apresente o estado atualizado do personagem.

name = "Frisk"
life = 100
gold = 150
lv = 4

gold += 5
print(name, "ganhou 5 moedas de ouro!")
print("Ouro:", gold)


print("\n")
print("===============================================")
life -= 10
print(name, "Recebeu 10 pontos de dano!")

print("\n======= Loja ========")
gold -= 40
print(name, "comprou uma adaga de ferrite.")
print("Ouro atual:", gold)


print("\n")
print("===============================================")
life += 10
print(name,"recuperou 10 pontos de vida")
print("\n")
print("===============================================")
lv += 1
print(name," subiu de nivel!!")
print("Nivel atual:", lv)


print("\n======== ", name ,"===========")
print("Ouro:", gold)
print("Vida:",life)
print("Nivel:", lv)
