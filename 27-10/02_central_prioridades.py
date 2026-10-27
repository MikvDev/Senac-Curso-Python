# A equipe dispõe de tempo limitado para analisar uma mensagem. As prioridades abaixo são regras fictícias para praticar decisões em Python.

# Recebam pelo teclado:

# a identificação da mensagem;
# o tempo disponível, em minutos, como decimal;
# o tempo necessário, em minutos, como decimal;
# a resposta à pergunta A mensagem indica risco imediato? (sim/nao):;
# a resposta à pergunta A mensagem contém uma pista recorrente? (sim/nao):.
# Regras de validação:

# Os dois tempos devem ser maiores que zero. Usem or para detectar um tempo inválido e mostrem Tempo inválido.
# As duas respostas devem ser exatamente sim ou nao. Se alguma não for, mostrem Resposta inválida.
# Não classifiquem a mensagem quando houver dados inválidos. Se houver erro nos tempos e nas respostas ao mesmo tempo, a mensagem de tempo inválido tem prioridade.


idMessage = input("Identifcação da mensagem: ")
timeRemaning = float(input("Tempo disponível: "))
timeNecessary = float(input("Tempo necessário: "))
isWarning = input("A mensagem indica risco imediato? (sim/nao): ").strip().lower()
isTrack = input("A mensagem contém uma pista recorrente? (sim/nao): ").strip().lower()

if timeRemaning <= 0 or timeNecessary <= 0:
    print("Tempo inválido.")
elif isWarning != "sim" and isWarning != "nao":
    print("Sua resposta foi inválida.")
elif isTrack != "sim" and isTrack != "nao":
    print("Sua resposta foi inválida.") 
elif timeNecessary > timeRemaning:
    print("Solicitar apoio: tempo insuficiente") 
elif timeNecessary <= timeRemaning and isWarning == "sim":
    print("Prioridade máxima.")
elif timeNecessary <= timeRemaning and isWarning == "nao" and isTrack == "sim":
    print("Prioridade alta.")
elif timeNecessary <= timeRemaning and isWarning == "nao" and isTrack == "nao":
    print("Prioridade normal.")
else: 
    print("Resposta inválida.")


# Para explicar: se há risco imediato, mas falta tempo, qual resultado aparece? Justifiquem com a ordem das condições e discutam por que um programa real precisaria de regras definidas por pessoas responsáveis por esse contexto.

# O resultado que vai aparecer é tempo insuficiente, pois cai na segunda verificação. Precisamos colocar testes para que o programa efetue o passo a passo das verificações necessarias.
