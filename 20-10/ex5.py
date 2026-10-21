# Durante uma aventura, um personagem encontra um inimigo e precisa decidir se consegue derrotá-lo.

# Solicite:

# Nome do personagem.
# Vida atual.
# Pontos de ataque.
# Vida do inimigo.
# Pontos de defesa do inimigo.
# Calcule o dano causado:


# Calcule o dano causado:

# dano = ataque - defesa
# Considere as seguintes regras:

# Se a vida do personagem for menor ou igual a zero, ele não poderá atacar.
# Se o dano for menor ou igual a zero, o ataque não causará dano.
# Se o dano for maior ou igual à vida do inimigo, o inimigo será derrotado.
# Caso contrário, o inimigo sobreviverá. Exiba a vida restante dele.
# Desafio: Impedir que a vida restante do inimigo fique negativa.




nomePersonagem = input("Digite o nome do personagem:")
vidaPersonagem = int(input("Digite a vida atual do seu persogem:"))
pontosDanoPersonagem = int(input("Digite de quantidade de pontos de ataque:"))
vidaInimigo = int(input("Digite qual a vida do inimigo:"))
pontosDeDefesa = int(input("Digite qual a defesa  do inimigo:"))




if vidaPersonagem <= 0:
    print("Vida do personagen esta muito baixa! Ele não podera atacar o inimigo")
elif pontosDanoPersonagem <= 0:
    print("Seu dano de ataque está muito baixo! Ele não causara dano no inimigo!")
elif pontosDanoPersonagem > vidaInimigo:
    dano = pontosDanoPersonagem - pontosDeDefesa
    vidaInimigo -= dano
    if vidaInimigo > 0:
        vidaInimigo = 0
    print("Inimigo derrotado!")
elif pontosDanoPersonagem <= vidaInimigo:
    dano = pontosDanoPersonagem - pontosDeDefesa
    vidaInimigo -= dano
    if vidaInimigo > 0:
        vidaInimigo = 0
    print("Vida restante do inimigo:")
    print(vidaInimigo)





