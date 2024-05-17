class Vehicle:
    def __init__(self):
        self.vehicle_type = None

    def __str__(self):
        return f'Мощность автомобиля {self}'


class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self, power):
        return self


class Nissan(Car, Vehicle):
    def __init__(self, model, price, vehicle_type):
        self.price = price
        self.vehicle_type = vehicle_type
        self.model = model

    def __str__(self, *args, **kwargs):
        return f'Автомобиль {__class__.__name__}, модель {self.model}, класса {self.vehicle_type}, стоимостью {self.price} руб.'

    def horse_powers(self, power):
        self.power = power
        return f'Мощность автомобиля {self.power} л.с'


patrol = Nissan(model='Patrol', price=7000000, vehicle_type='SUV')
print(patrol)
print(patrol.horse_powers(280))
