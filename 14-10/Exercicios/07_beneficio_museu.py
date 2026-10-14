# Leia uma idade não negativa. Neste museu fictício, pessoas com menos de 12 anos ou a partir de 60 anos têm entrada gratuita. As demais pagam R$ 20.00.

# Use or e teste as idades 11, 12, 59 e 60.

user_age = int(input("Digite sua idade:"))
if user_age < 12 or user_age >= 60:
    print("Entrada gratuita!")
else:
    print("Entrada paga")