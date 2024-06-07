class Car:
    def __init__(self, price=1000000):
        self.price = price

    def horse_powers(self):
        print(100, 'h.p.')


class Nissan(Car):
    price = 3000000

    def horse_powers(self):
        print(300, 'h.p.')


class Kia(Car):
    self.price = 2000000

    def horse_powers(self):
        print(200, 'h.p.')


car_1 = Car()
car_2 = Nissan()
car_3 = Kia()
print(car_1.price)
car_1.horse_powers()
print(car_2.price)
car_2.horse_powers()
print(car_3.price)
car_3.horse_powers()