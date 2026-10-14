# Crie uma variável chamada informacao. Ela deverá receber, nesta ordem:

# o texto "42";
# o número inteiro 42;
# o número decimal 42.0;
# o valor booleano False.
# Após cada atribuição, mostre o valor e o resultado de type(informacao).

# Escreva um comentário explicando a diferença entre "42" e 42. Ao final, explique se a variável guarda os quatro valores ao mesmo tempo ou apenas o último valor atribuído.
informacao = "42"
type(informacao) # str, string - Texto
informacao = 42
type(informacao) # int, inteiro - Numero
informacao = 42.0
type(informacao) # float, decimal - Numero
informacao = False
type(informacao) # bool, booleano - Valor lógico

# A diferença entre "42" e 42 é que o primeiro é uma string (texto) e o segundo é um número inteiro. A variável informacao guarda apenas o último valor atribuído, ou seja, False.