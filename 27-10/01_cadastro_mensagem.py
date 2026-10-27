# Recebam pelo teclado:

# o nome ou apelido do analista;
# a identificação da mensagem, como texto, por exemplo MSG-007;
# a quantidade de grupos de símbolos, como inteiro;
# o tempo estimado para analisar cada grupo, em minutos, como decimal.
# Regras:

# A quantidade de grupos e o tempo por grupo devem ser maiores que zero.
# Se qualquer um desses valores for inválido, mostrem Dados inválidos e não calculem o tempo total.
# Se os dados forem válidos, calculem o tempo total estimado: quantidade de grupos multiplicada pelo tempo por grupo.
# Apresentem uma ficha com o analista, a identificação, a quantidade de grupos e o tempo total em minutos.
# Se o total for menor ou igual a 60 minutos, mostrem Análise dentro do prazo; caso contrário, mostrem Reorganizar o trabalho.
# Para explicar: por que a identificação é texto mesmo quando contém algarismos? Por que é adequado usar float() para o tempo por grupo?


#  
nameAnalist = input("Digite o nome do analista:")
idMessage = input("Qual o ID da mensagem:")
integerGroups = int(input("Digite a quantidade de números de grupos de simbolos:"))
timeAnalist = float(input("Digite a quantidade de tempo que será necessária para concluir a analise:  "))


if integerGroups < 0 or timeAnalist < 0:
    print("Dados inválidos.")
else:
    countTimEestimated = integerGroups * timeAnalist
    
    print("=====FICHA=====\n")
    print(f"Nome do analista: {nameAnalist}.")
    print(f"Identificação da mensagem: {idMessage}.")
    print(f"Quantidade de grupos: {integerGroups}.")
    print(f"Tempo total: {countTimEestimated} min.")
    print("=================")

    if countTimEestimated <= 60:
        print("Análise dentro do prazo")
    else:
        print("É necessario organizar o fluxo de trabalho")


# Por que String? Porque quando recebermos uma identificação da mensagem ela pode vir com numeros e letras, como string não vai ocorrer erro de compilação. Também é util usar string poís não vamos fazer calculos com o id e não vamos correr o risco de perder numeros de identificação caso o usuário digite "007"(em inteiro vira 7)
# É adequado utilizar o float(), por que pode ser que o tempo seja em segundos ou em horas e queremos saber quanto tempo será em minutos, além de que pode ser a metade do tempo.