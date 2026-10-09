# Quatro amigos compraram uma pizza de R$ 48.00 e uma bebida de R$ 12.00. A conta será dividida igualmente.

# Crie variáveis para o preço da pizza, o preço da bebida e a quantidade de amigos.
# Calcule o total da conta em uma nova variável.
# Calcule quanto cada amigo deverá pagar.
# Mostre o total e o valor por pessoa com descrições.
# Use type() para mostrar o tipo do valor por pessoa.
# Para pensar: o resultado da divisão é um int ou um float, mesmo quando não há centavos?


# Exercicio

precoPizza = 48.00
precoBebida = 12.00
quantidadeDeAmigos = 4


# Calculo conta

contaTotalCalculo = precoBebida + precoPizza
valorAPagarAmigos = contaTotalCalculo / quantidadeDeAmigos
print("Cada amigo irá pagar: " + str(valorAPagarAmigos))
print(type(valorAPagarAmigos)) 
print("Resposta: O valor será  um float, pois definimos o valor das variaveis no começo como sendo um float(bebida e pizza), mesmo dividindo por um inteiro ao final elas ainda vão continuar sendo um float")

