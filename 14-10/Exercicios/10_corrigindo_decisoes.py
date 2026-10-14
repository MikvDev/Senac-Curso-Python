idade = int(input("Idade: "))
autorizacao = input("Possui autorização? (sim/nao): ")

if idade >= 16 and autorizacao == "sim":
    print("Participação permitida.")
else:
    print("Participação não permitida.")