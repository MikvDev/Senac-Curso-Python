# Um laboratório de tecnologia possui equipamentos que só podem ser utilizados por pessoas autorizadas.

# Solicite:

# Idade.
# Se a pessoa é aluno matriculado (sim ou nao).
# Se possui autorização do professor (sim ou nao).
# Se o laboratório está disponível (sim ou nao).
# O acesso será permitido quando:

# O laboratório estiver disponível.
# A pessoa tiver pelo menos 16 anos.
# A pessoa for matriculada ou possuir autorização do professor.
# Requisitos: Utilize and e or e apresente uma mensagem indicando se o acesso foi permitido ou negado.

idade = int(input("Digite sua idade:"))
alunoMatriculado = input("Você está matriculado(sim/nao):")
autorizacaoProfessor = input("Possui autorização do seu professor(sim/nao):")
laboratorioDisponivel = input("Laboratório está disponivel(sim/nao):")

if laboratorioDisponivel == "sim" and idade > 16 and (alunoMatriculado == "sim" or autorizacaoProfessor == "sim"):
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")    