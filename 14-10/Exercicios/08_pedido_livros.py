# A biblioteca tem 8 exemplares disponíveis. Leia a quantidade que a pessoa deseja retirar.

# Se a quantidade for menor ou igual a zero, informe que o pedido é inválido.
# Se for maior que o estoque, informe que não há exemplares suficientes.
# Caso contrário, confirme o pedido, atualize o estoque e mostre a quantidade restante.
# O estoque só deve diminuir quando o pedido for confirmado.

stock_quantity = 8

book_quantity = int(input("Digite a quantidade desejada para retirar os livros:"))
if book_quantity <= 0:
    print("Pedido é invalido")
elif book_quantity > stock_quantity:
    print("Pedido é maior que estoque.")
else:
    print("Pedido confirmado!")
    stock_quantity -= book_quantity
    print(f"Quantidade no estoque {stock_quantity}")