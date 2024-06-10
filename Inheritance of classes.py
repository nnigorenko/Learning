class Car:
    def __init__(self, price=1000000, power=100):
        self.price = price
        self.power = power

    def horse_powers(self):
        return self.power

class Nissan(Car):
    def horse_powers(self):
        if Car().power < self.power:
            print("More powerful than average!")
        return self.power


class Kia(Car):

    def horse_powers(self):
        print(f"My power is {self.power} h.p.")
        return self.power


car_1 = Car()
car_2 = Nissan(3000000, 300)
car_3 = Kia(2000000, 200)
print(car_1.price, car_1.horse_powers())
print(car_2.price, car_2.horse_powers())
print(car_3.price, car_3.horse_powers())
