# Crie uma loja com atendimento de uma única compra por execução.

# Leia o nome do aventureiro e sua quantidade de ouro, como número inteiro.
# Se o ouro for negativo, mostre Quantidade de ouro inválida e não prossiga com a compra.
# Caso contrário, mostre um menu: 1 para poção de vida (25 moedas), 2 para escudo (60 moedas) e 3 para espada (100 moedas).
# Leia a opção como texto e verifique se ela existe.
# Para uma opção válida, verifique se o ouro é suficiente. Se for, desconte o preço e mostre o item adquirido e o saldo restante. Caso contrário, informe quantas moedas faltam.
# Se a opção não existir, mostre Item inválido.
# O ouro só pode ser descontado quando a compra for confirmada. Teste uma compra com sobra de ouro, uma com o valor exato, outra com saldo insuficiente, uma opção inválida e um saldo inicial negativo.

user_name = input("Digite seu nome:")
user_gold = int(input("Digite sua quantidade atual de ouro:"))

if user_gold < 0:
    print("Quantidade de ouro insuficiente!")
else:
    print("======= Menu =============")
    print("1 - poção de vida (25 moedas)")
    print("2 - escudo (60 moedas)")
    print("3 - espada (100 moedas).")

option = input("Digite qual item deseja adquirir:")
if option == "1":
    if user_gold >= 25:
        user_gold -= 25
        print("Item adquirido: poção de vida")
        print("Saldo restante:", user_gold)
    else:
        faltam = 25 - user_gold
        print(f"Saldo insuficiente! Faltam {faltam} moedas.")
    print("Saldo restante:", user_gold)
elif option == "2":
    if user_gold >= 60:
        user_gold -= 60
        print("Item adquirido: escudo")
        print("Saldo restante:", user_gold)
    else:
        faltam = 60 - user_gold
        print(f"Saldo insuficiente! Faltam {faltam} moedas.")
    print("Saldo restante:", user_gold)
elif option == "3":
    if user_gold >= 100:
        user_gold -= 100
        print("Item adquirido: espada")
        print("Saldo restante:", user_gold)
    else:
        faltam = 100 - user_gold
        print(f"Saldo insuficiente! Faltam {faltam} moedas.")
    print("Saldo restante:", user_gold)
