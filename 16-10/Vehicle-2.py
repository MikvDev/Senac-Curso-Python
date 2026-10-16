# Escreva um programa em Python para criar uma Vehicleclasse com dois atributos de instância: `atributos` max_speede `btributes` mileage. Crie um objeto da classe e imprima ambos os atributos.

class Vehicle:
    def __init__(self, max_speed, mileage, brand):
        self.max_speed = max_speed
        self.mileage = mileage
        self.brand = brand
    def __str__(self):
        return f"Vehicle Name:{self.brand}, Speed: {self.max_speed}, Mileage: {self.mileage}"

print(Vehicle(250, 18, "Tesla Model S"))