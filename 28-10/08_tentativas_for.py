# Defina o código fictício "ROBO123". Dê ao usuário no máximo três tentativas para acertá-lo.

# Mostre o número da tentativa antes de cada leitura. Se acertar, encerre o laço com break e informe o sucesso. Se errar todas, informe que as tentativas acabaram.

# Teste um acerto na primeira tentativa, um acerto na terceira e três erros.

code = "ROBO123"
isCodeCorrect = False

for tentativa in range(3,0,-1):
    userCode = input("Digite a senha: ")
    if userCode == code:
        print("Acesso permitido. Seja bem vindo.")
        isCodeCorrect = True
        break
    else:
        print("Tente novamente - você possui mais", tentativa - 1, "tentativas")
        continue

if isCodeCorrect != True:
    print("Acesso negado. Entrada não permitida.")
        





