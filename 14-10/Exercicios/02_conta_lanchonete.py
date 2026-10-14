# Leia o preço de um lanche e a quantidade comprada. Calcule o total. Considere preço e quantidade positivos. Se o total for a partir de R$ 50.00, aplique 10% de desconto; caso contrário, mantenha o valor original.

# Mostre o total antes do desconto, o desconto e o valor final. Para calcular 10%, multiplique o total por 0.10. Teste totais abaixo de 50, iguais a 50 e acima de 50.

lauch_price  = float(input("Digite o valor do lanche:"))
lauch_quantity = int(input("Digite a quantidade comprada:"))
lauch_price_total = lauch_price * lauch_quantity
if lauch_price_total >= 50.00:
    lauch_descont = lauch_price_total * 0.10
    lauch_price_total -= lauch_descont
    print("Valor total:", lauch_price_total)
else:
    print("Valor total do pedido:", lauch_price_total)
