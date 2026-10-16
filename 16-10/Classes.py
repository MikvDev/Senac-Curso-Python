
# ------------------ Clases ------------------------ #
# Estruturas de dados definida pelo usuário 

# Usamos a palavra 'class' para criarmos uma classe.
# def __init__ para iniciar o construtor.  | initialize  

# ------------------ Classe User ------------------------ #
class User:
    def __init__(self, name, age): # sempre o primeiro parametro será self(ou qualquer outro termo )
        self.name = name
        self.age = age
# O self diz 'this' - isso, este, neste... Este atributo recebe isto como valor do paremetro.
# ------------- Classe test ------------------------------ # 
class test:
    pass# Isso serve para não dar erro por não ter nada dentro da classe.

# ------------------ Classe Dog ------------------------ #
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, race, age): # 4 espaços para criar o __init__ \ Identação
        self.name = name
        self.race = race 
        self.age = age
    # Tudo dentro dessa classe pertence a ela.
    def bark(self):
        return f"{self.name}: Auau!"
    def __str__(self):  # Metodo Dunder - Começam com dois __  e terminam em __
        return f"Nome: {self.name} | Raça: {self.race} | Idade: {self.age}  "


# ------------------ Classe Veiculo --------------------- # 

class Veiculo:
    has_door = True
    



# ------------------ Classe Car ------------------------ #

class Car(Veiculo):
    def __init__(self, brand, price, color, mileage):
        self.brand = brand
        self.price = price
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f"The {self.color} car has {self.mileage:.3f} miles | {self.has_door}"

# ------------------ Metodos -------------------------- #
# __str__()e seu primo .__repr__().

# ------------------ Instancias ------------------------ #

# loki = Dog("Loki","canino", 3)
# rex = Dog("Rex", "Labrador", 4)

# print(rex.bark())
# print(loki)

blue = Car("Fiat", 60.000,"Blue",20.000,)
red = Car("Corola", 260.000,"Red",30.000,)


for car in(blue, red):
    print(car)


# ----------- Herdar atributos --------- #

# É muito simples herdar atributos, é só colocar dentro do parentese da classe criada de qual classe você gotaria de puxar os atributos .
# class Funcionario(User) - vai herdar tudo da classe user.

