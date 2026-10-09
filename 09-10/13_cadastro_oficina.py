nomeOficina = "Robótica para iniciantes"
sala = "Laboratório 2"
QuantidadeVagas = 24
duracaoHoras = 2.5
inscricaoAbertas = True


# textos devem ser colocados entre aspas para serem uma variavel 'str'
# Numeros inteiros devem ser atribuidos a uma varivel sem o uso de aspas, assim ela sera um 'int'(inteiro)
# Numreos double são numeros com casa decimal, para definir um variavel como double 
print("===============================")
print("Nome oficina: " + nomeOficina)
print(type(nomeOficina)) # Variavel de texto
print("Sala: " + sala)
print(type(sala)) # Variavel de texto
print("Quantidade de Vagas: " + str(QuantidadeVagas))
print(type(QuantidadeVagas)) # Numeros inteiros 
print("Duração (horas): " + str(duracaoHoras))
print(type(duracaoHoras)) # Numero com casas decimais(horas, preço...)
print("Inscrições Abertas: " + str(inscricaoAbertas))
print(type(inscricaoAbertas)) # boleano - verdadeiro ou falso
print("===============================")