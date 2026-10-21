# Um banco deseja automatizar a análise inicial de empréstimos.

# Solicite as seguintes informações:

# Salário mensal do cliente.
# Valor solicitado para empréstimo.
# Quantidade de parcelas.
# O empréstimo só poderá ser aprovado se todas as condições forem atendidas:

# O salário deve ser de pelo menos R$ 2.000,00.
# O valor solicitado não pode ultrapassar 10 vezes o salário.
# O valor de cada parcela não pode ultrapassar 30% do salário.
# A quantidade de parcelas deve estar entre 1 e 48.
# Caso alguma condição não seja atendida, informe que o empréstimo foi recusado.

# Desafio: Apresente o motivo da recusa.

# Considere um empréstimo sem juros, apenas para fins de exercício.

salario_mensal = float(input("Digite seu salário mensal:"))
emprestimo_solicitado = float(input("Digite o valor desejado para o emprestimo: "))
quantidade_parcelas = int(input("Digite a quantidade de parcelas:"))

if salario_mensal >= 2000:
    if  salario_mensal > (emprestimo_solicitado * 10) :
        print("Valor não pode ultrapassar 10 vezes seu salário")
    elif(emprestimo_solicitado / quantidade_parcelas) > (salario_mensal * 0.30):
       print("Valor não pode ultrapassar 30% do salario")
    elif quantidade_parcelas >= 1 and  quantidade_parcelas <= 48:
            valorParcelas = emprestimo_solicitado / quantidade_parcelas
            print("================================")
            print(f"Emprestimo: {emprestimo_solicitado:.2f}")
            print(f"Parcelas: {quantidade_parcelas}")
            print(f"Valor por parcelas: {valorParcelas:.2f}")
            print("================================")

    else:
            print("Imprestimo recusado! Quantidade de parecelas é maior que 50")

else:
    print("Seu salário é inválido - Salário minimo é 2.000!")