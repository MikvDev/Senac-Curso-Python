# Um robô pode realizar até cinco missões. Ele começa com 100 pontos de energia, e cada missão custa 25 pontos.


# Após receber uma pontuação válida, desconte a energia, acumule os pontos e conte a missão realizada.
# Ao final, mostre a quantidade de missões realizadas, a pontuação total, a média de pontos por missão realizada e a energia restante. Só calcule a média se houver pelo menos uma missão realizada.
# Teste de mesa: com pontuações 80, 60, 100 e 40, o robô deve completar quatro missões, somar 280 pontos, obter média 70.0 e terminar com energia 0. A quinta missão não deve solicitar pontuação.

# Desafio adicional: altere a energia inicial para 20. O programa deve encerrar sem realizar missões e sem tentar dividir por zero.

energy = 20
missionPoints = 0
totalMissionPoints = 0
missionCompleted = 0
avaragePointsMissions = 0
if energy < 25:
    print("ENERGIA INSUFICIENTE")
else:

    for mission in range(1,6):
       missionPoints = int(input("Digite a pontuação da missão <| 0 a 100 |> : "))
       while missionPoints < 0 or missionPoints > 100:
           print("Valor invalido! Digite novamente.")
           missionPoints = int(input("Digite a pontuação da missão <| 0 a 100 |> : "))
       totalMissionPoints += missionPoints
       energy -= 25
       missionCompleted += 1
       if energy >= 25:
               continue
       else: 
           print("ENERGIA INSUFICIENTE")
           break

if  missionPoints <= 0 and missionCompleted <= 0:
      print("Valores inválidos para calcular media de pontos")

else :
     avaragePointsMissions = missionPoints / missionCompleted
print("\n=====================================")
print("MISSÕES REALIZADAS:", missionCompleted)
print("TOTAL DE PONTOS:", totalMissionPoints)
print("MEDIA DE PONTOS:", avaragePointsMissions)
print("ENERGIA RESTANTE:", energy)
print("\n=====================================")

        

