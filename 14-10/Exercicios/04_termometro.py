# Leia uma temperatura e mostre apenas uma classificação:

# abaixo de 18: Ambiente frio;
# a partir de 18 e abaixo de 26: Ambiente agradável;
# a partir de 26: Ambiente quente.
# Teste especialmente os valores 18 e 26.

temperature = int(input("Digite o valor da temperatura:"))
if temperature < 18:
    print("Ambiente frio")
elif temperature > 18 and temperature < 26:
    print("Ambiente agradavel")
elif temperature > 26:
    print("Ambiente quente")