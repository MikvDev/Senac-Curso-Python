# Você vai simular uma missão utilizando apenas variáveis e operações sequenciais.

# Crie o estado inicial do robô:

# Informação	Valor inicial
# Nome	"Atlas"
# Energia	100
# Distância percorrida, em metros	0
# Amostras coletadas	0
# Missão em andamento	True
# Mostre uma ficha inicial. Depois simule os acontecimentos nesta ordem:

# O robô percorre 120 metros e consome 20 pontos de energia.
# Coleta 3 amostras e consome 15 pontos de energia.
# Recarrega 10 pontos de energia.
# Percorre mais 80 metros e consome 25 pontos de energia.
# Coleta mais 2 amostras e consome 10 pontos de energia.
# Encerra a missão: atribua False à variável que indica se a missão está em andamento.
# Atualize as variáveis correspondentes em cada etapa. Mostre uma mensagem após cada acontecimento e, no final, apresente uma ficha com todos os valores atualizados.

# Parte extra: considerando que a missão durou 4 minutos, calcule a distância média percorrida por minuto e mostre o resultado com a unidade metros por minuto.

robot_name = "Atlas"
robot_energy = 100
distance_traveled = 0
samples_collected = 0
mission_ongoing = True

print("Ficha inicial do robô:")
print("Nome:", robot_name)  
print("Energia:", robot_energy)
print("Distância percorrida:", distance_traveled, "metros")
print("Amostras coletadas:", samples_collected)
print("Missão em andamento:", mission_ongoing)

print("\n==========================================================")
print("O robô percorre 120 metros e consome 20 pontos de energia.")
robot_energy -= 20
distance_traveled += 120
print("Energia:", robot_energy)
print("\n==========================================================")

print("\n==========================================================")
print("Coleta 3 amostras e consome 15 pontos de energia.")
robot_energy -= 15
samples_collected += 3
print("Energia:", robot_energy)
print("Amostrar coletadas:", samples_collected)
print("\n==========================================================")

print("\n==========================================================")
print("Recarrega 10 pontos de energia.")
robot_energy += 10
print("Energia:", robot_energy)
print("\n==========================================================")

print("\n==========================================================")
print(" Percorre mais 80 metros e consome 25 pontos de energia.")
distance_traveled += 80
robot_energy -= 25
print("Energia:", robot_energy)
print("\n==========================================================")

print("\n==========================================================")
print("Coleta mais 2 amostras e consome 10 pontos de energia.")
robot_energy -= 10
samples_collected += 2
print("Energia:", robot_energy)
print("Amostrar coletadas:", samples_collected)
print("\n==========================================================")

print("\n==========================================================")
print("Encerra a missão: atribua False à variável que indica se a missão está em andamento.")
mission_ongoing = False
print("Missão finalizada!")
print("\n==========================================================")

mission_time = 4
total_meters = 200
average_distance = total_meters / mission_time
print("Metros por minuto percorrido pelo robo:", average_distance) 


print("\n==========================================================")
print("Ficha final do robô:")
print("Nome:", robot_name)  
print("Energia:", robot_energy)
print("Distância percorrida:", distance_traveled, "metros")
print("Amostras coletadas:", samples_collected)
print("Missão em andamento:", mission_ongoing)