# Escreva um programa em Python para criar uma Rectangleclasse com length`a` e ` widthp` como atributos de instância, e dois métodos: area()um que retorna a área e perimeter()outro que retorna o perímetro.
class Retangle:
  
    def area(self, width, length): # Tem que passar o self 
        area = width * length
        return f"Area do retangulo: {area} "
    def perimetro(self, width, length):
        calc_perimetro = width + length
        return f"Perimetro do retangulo: {calc_perimetro}" 

r1 = Retangle()
print(r1.area(10,10))
print(r1.perimetro(20,20))
        