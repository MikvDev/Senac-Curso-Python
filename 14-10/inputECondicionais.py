# # Inputs e condicionais 


# # Input sempre devolve string, então é necessário converter para o tipo desejado.

# numero1 = input("Digite o numero 1:")
# numero2 = input("Digite o numeor 2:")

# print("Numeros", numero1 + numero2)


# # Podemos mudar o tipo da variavel
# number = int(input("Digite o numero:"))
# print(type(number))


# nome = input("Qual é o seu nome?")
# print("Olá",nome)

# # Cadastro simples 

# user_name = input("Digite seu nome de usuário:")
# user_adress = input("Digite seu endereço de e-mail:")
# user_password = input("Digite sua senha:")

# print("Cadastro realizado com sucesso!")


# print("\n============ Perfil ===============")
# print("Nome de usuário:", user_name)
# print("Endereço de e-mail:", user_adress)   
# print("Senha:", user_password)


# =========================================


# # Numeros decimais - Float 
# nome = input("Digite o nome: ")
# preco = float(input("Preço do produto: "))
# quantidade = int(input("Quantidade: "))

# total = preco * quantidade

# print("Total da compra:", total)

# int(input("Numero inteiro:"))
# float(input("Numero com virgula: "))


# # Format string | Template string 
# print(f"Olá {nome}, seja bem vindo(a)!")



# Condicionais 


# Condicionais servem para controlarmos o fluxo da aplicação. Nesse caso, estamos verficando se o usuário possui mais de 18 anos.
idade = 18
print(idade >= 18)

# Operadores de comparação

# Operador == (igual a), pode comparar duas variaveis.
# Operador != (diferente), compara se as variavies são diferentes.
# Operador >(maior que), compara se a variavel é maior que determinada variavel.
# Operador <(menor que), compara se a variavel é menor que determidada variavel.
# Operador >=(maior igual), compara se a variavel é maior e igual a variavel.
# Operador <=(menor igual), compara se a variavel é menor é igual a variavel.


# = - atribui, e == compara 

# Compare:


# idade = 18          # Atribui um valor.
# print(idade == 18)   # Compara o valor e mostra True.

# idade = 18
# print(idade == 18)


# # Também podemos comparar textos 
# resposta = input("Deseja continuar? Digite sim ou não:")
# print(resposta == "sim")


# if

# Em python usamos a identação para controlar o escopo de blocos de codigos 
# # Se for verdade é mostrado a mensagem no terminal, se não 
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Parabens! Você é uma adulto agora!")
# else:
#     print("Que droga cara! Infelizmente você ainda não tem 18 anos.")
# print("Codigo encerrado!")


# # Identação 

# # Como disse, em python usamos a identação e : para definirmos bloco de codigos, inves de {}.

# energia  = int(input("Digite a energia do robo:"))
# if energia < 20: # Dois pontos utilizado, este bloco pertence ao if
#     print("Recarregue seu robo")
#     print("Sua energia está baixa!")
# print("Verificação concluida!")


#  if e else 


# quantidade = int(input("Quantidade disponivel em estoque:"))
# if quantidade > 0:
#     print(f"O estoque possui {quantidade} itens.")
# else:
#     print("O estoque esta vazio!")


# Elif 

# media = float(input("Digite sua media do trimestre:"))
# if media >= 6:
#     print("Aprovado")
# elif media < 6:
#     print("Em recuperação")
# else:
#     print("Reprovado")


# Qual diferença entre usar if e elif? varios if um abaixo do outro vão fazer todas as verificações, já um if e elif podemos ter apenas uma resposta, não varias.


# And

# And seria o &&, preciamos que 2 valores sejam true para termos um valor true.

# idade = int(input("Digite sua idade:"))
# vagas = int(input("Digite a quantidade de vagas do curso:"))

# if idade >= 18 and vagas > 0:
#     print("Parabens! Você está participando do curso!")
# else:
#     print("Infelizmente, não podemos aceitar sua incrição.")

# Or, ou, se uma for verdade, temos uma verdade.
# idade = int(input("Digite sua idade:"))
# vagas = int(input("Digite a quantidade de vagas do curso:"))

# if idade >= 18 and vagas > 0:
#     print("Parabens! Você está participando do curso!")
# else:
#     print("Infelizmente, não podemos aceitar sua incrição.")


# idade = 14
# cargo = "professor"
# # Uma verdade se o usuário tiver mais de 14 anos, e uma verdade se for aluno ou professor.
# if idade >=  14 and  (cargo == "aluno" or cargo == "professor"):
#     print("Entrada aceita!")


# Usando not 
# Ele inverte o valor boleano.
# True - false
# false - true

# resposta  = input("O robo está em manutençaõ? (sim/não): ")
# em_manutencao = resposta == "sim"

# if not em_manutencao:
#     print("Robo está disponivel")
# else:
#     print("Robo está em manutenção")


# # Condicionais dentro de condicionais 

# quantidade  = int(input("Digite a quantidade desejada:"))
# estoque = 10

# if quantidade > 0:
#     if quantidade <= estoque:
#         estoque -= quantidade
#         print("Pedido confirmado!")
#         print(f"Estoque restanate {estoque}")
#     else:
#         print("Quantidade é maior que estoque.")
# else:
#     print("A quantia deve ser maior que 0.")


# Exemplo 

# nome = input("Nome do robô: ")
# energia = int(input("Energia atual (0 a 100): "))
# resposta = input("Está em manutenção? (sim/nao): ")

# print("=== CENTRAL DE MISSÕES ===")
# print("Robô:", nome)

# if energia < 0 or energia > 100:
#     print("Energia inválida. Informe um valor entre 0 e 100.")
# elif resposta != "sim" and resposta != "nao":
#     print("Resposta inválida. Use sim ou nao.")
# else:
#     em_manutencao = resposta == "sim"

#     if energia >= 50 and not em_manutencao:
#         print("Missão autorizada.")
#         energia = energia - 30
#         print("Energia após a missão:", energia)
#     elif em_manutencao:
#         print("Missão bloqueada: robô em manutenção.")
#     else:
#         print("Missão bloqueada: energia insuficiente.")

# print("Atendimento encerrado.")


# Desafio 

# nota = float(input("Nota: "))

# if nota >= 5:
#     print("Primeira condição atendida.")

# if nota >= 7:
#     print("Segunda condição atendida.")
# else:
#     print("Segunda condição não atendida.")

# print("Fim.")

# As duas condições vão aparecer   print("Primeira condição atendida.") e print("Segunda condição atendida."). 


nota = float(input("Nota: "))

if nota >= 5:
    print("Primeira condição atendida.")

elif nota >= 7:
    print("Segunda condição atendida.")
else:
    print("Segunda condição não atendida.")

print("Fim.")

# Apenas um dos caminhos vai ser seguido - print("Primeira condição atendida.")