class Car:
    """Автомобиль"""

    def __init__(self):
        self.price = 1000000

    def horse_powers(self=None):
        return self


class Nissan(Car):
    def __init__(self, price):
        self.price = price

    def horse_powers(self):
        max_power = self
        print(f'Моя машина {__class__.__name__}, Мощность {max_power} л.с., Цена {my_second_car.price} руб.')
        return max_power


class Kia(Car):
    def __init__(self, price):
        self.price = price
    def horse_powers(self):
        max_power = self
        print(f'Моя машина {__class__.__name__}, Мощность {max_power} л.с., Цена {my_first_car.price} руб.')
        return max_power


my_first_car = Kia(price=2800000)
my_first_car.__class__.horse_powers(170)
my_second_car = Nissan(3500000)
my_second_car.__class__.horse_powers(250)
