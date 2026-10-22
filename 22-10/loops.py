## ---------- Estruturas de repetição ---------- ##


# Loops são estruturas de repetição que permitem executar um bloco de código várias vezes, enquanto uma condição for verdadeira. Existem dois tipos principais de loops em Python: o loop "for" e o loop "while".

# ------ while Loop ------ #

contador = 0




# 
while contador <= 5:
    print(f"Contador {contador}")
    contador += 1
    # contador = contador + 1 

    
print("Fim do código")

while True:
    resposta = input("Digite contiunar? (sim/nao)")
    if resposta == "nao":
        break
    print("Continuando!")
print("Programa finalizado")

print("============================================")
print("1 - Perfil")
print("2 - Posts")
print("3 - Notificação")

optionMenu = int(input("Digite a opção desejada:"))    

while optionMenu !=0:


    

    if optionMenu == 1:
        print("\n====================")
        print("1 - Nome:")
        print("1 - Bio:")
        print("====================")
        optionMenu = int(input("Digite a opção desejada:"))   
    elif optionMenu == 2:
        print("====================")
        print("")
    elif optionMenu == 0:
        print("Saindo!")

# ----- for Loop ----- #


 
