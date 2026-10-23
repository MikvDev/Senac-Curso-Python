
import os
import time
# Crie um menu com as seguintes opções:

# === MENU ===
# 1 - Somar dois números
# 2 - Verificar maioridade
# 0 - Sair

# O menu deverá continuar aparecendo até o usuário escolher a opção 0.

# Utilize while True, condicionais e break.

while True:
    os.system('cls' if os.name == 'nt' else clear)
    print("=== MENU ===")
    print("1 - Somar dois números")
    print("2 - Verificar maioridade")
    print("0 - Sair")
    op = int(input("Digite qual opção deseja:"))
    temMaiorIdade = False
    if op == 1:
        print("Somando dois numeros... 2 + 2 = 4")
        time.sleep(4)
    elif op == 2:
        temMaiorIdade = input("Voce possui +18 (sim/nao):")
        if temMaiorIdade == "sim":
            print("Acesso permitido!")
        else:
            print("Acesso negado!")
        time.sleep(4)
    elif op == 0:
        print("Saindo...")
        break
    else:
        print("Numero invalido!")

    
