# Uma loja virtual deseja calcular o valor do frete com base na região do cliente e no valor da compra.

# Solicite o valor da compra e a região de entrega:

# Região	Frete
# Sul	R$ 15,00
# Sudeste	R$ 20,00
# Centro-Oeste	R$ 25,00
# Norte ou Nordeste	R$ 35,00
# Regras adicionais:

# Compras a partir de R$ 300,00 recebem frete grátis.
# Compras com valor menor ou igual a zero são inválidas.
# Regiões não reconhecidas devem apresentar Região inválida.
# Mostre o valor da compra, o frete e o total.
# Atenção: Mesmo que a compra tenha frete grátis, a região informada deverá ser válida.

comprasValor = float(input("Digite o valor da compra:"))
regiaoEntrega = input("Digite qual sua região:")


if comprasValor <= 0 :
    print("compra invalida")
else:
    if regiaoEntrega == "Sul":
        if comprasValor >= 300:
            print("Parebens você ganhou frete gratis!")
        else:
            print("valor do frete: 15")
            print(f"Valor total: {comprasValor + 15}")
    elif regiaoEntrega == "Sudeste":
            if comprasValor >= 300:
                print("Parebens você ganhou frete gratis!")
            else:
                print("valor do frete: 15")
                print(f"Valor total: {comprasValor + 20}")
    elif regiaoEntrega == "Centro-Oeste":
                if comprasValor >= 300:
                    print("Parebens você ganhou frete gratis!")
                else:
                    print("valor do frete: 15")
                    print(f"Valor total: {comprasValor + 25}")
    elif regiaoEntrega == "Norte" or regiaoEntrega == "Nordeste":
                if comprasValor >= 300:
                    print("Parebens você ganhou frete gratis!")
                else:
                    print("valor do frete: 15")
                    print(f"Valor total: {comprasValor + 35}")
    else:
        print("Região invalida!")
    

