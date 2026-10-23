import os
import time
accountBalance = 500.00
while True:

    
    
    os.system('cls' if os.name == 'nt' else clear)
    print("=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("0 - Sair")

    option = int(input("\nDigite a opção que deseja: "))

    if option == 1:
        print(f"\nSaldo na conta:{accountBalance}")
        time.sleep(4)
    elif option == 2:
        deposit = float(input("Digite quanto deseja depositar:"))
        if deposit < 0:
            print("Valores negativos são invalidos!")
        
        accountBalance += deposit
        time.sleep(4)
    elif option == 3:
        takeMoney = float(input("Digite a quantidade que deseja sacar: "))
        if takeMoney > accountBalance:
            print("Quantidade excede valor em depositado no conta!") 
        else:
            print(f"Valor sacado: {takeMoney}")
            print(f"Valor na conta: {accountBalance - takeMoney}")
            accountBalance = accountBalance - takeMoney

         
        time.sleep(4)      





