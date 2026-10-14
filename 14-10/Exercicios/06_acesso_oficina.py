# Leia a idade e pergunte se a pessoa possui inscrição (sim/nao). Considere idade não negativa e uma das duas respostas indicadas. A entrada só será permitida para quem tiver pelo menos 14 anos e inscrição confirmada.

# Use and. Teste uma pessoa que atende aos dois critérios, outra que atende a apenas um e outra que não atende a nenhum.

user_age = int(input("Digite sua idade:"))
user_has_inscription = input("Digite (sim/nao) para se possui inscrição")

if user_age > 14 and user_has_inscription == "sim":
    print("Inscrição confirmada")
else:
    print("Inscrição recusada")