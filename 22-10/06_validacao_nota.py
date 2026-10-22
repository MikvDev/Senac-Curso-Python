# Solicite uma nota entre 0 e 10.

# Enquanto o usuário informar um valor fora desse intervalo, apresente Nota inválida e solicite novamente.

# Quando uma nota válida for informada, mostre Nota registrada com sucesso!.



while True:
    grade = float(input("Digite o valor da nota: "))
    if grade >= 0 and grade <= 10:
        print(f"Nota registrada: {grade}")
    else:
        print("Valor invalido!")
        break
   
        
