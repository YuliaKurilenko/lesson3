class Car:
    price = 1000000
    def horse_powers(self):
        return 200
        print()

    def inspect(self):
        print("Цена:", self.price)
        print("Количесво лошадиных сил:", self.horse_powers())

class Nissan(Car):
    price = 2000000
    def horse_powers(self):
        return 300
        print()
    def inspect(self):
        print("Цена:", self.price)
        print("Количесво лошадиных сил:", self.horse_powers())
class Kia(Car):
    price = 1500000
    def horse_powers(self):
        return 250
        print()
    def inspect(self):
        print("Цена:", self.price)
        print("Количесво лошадиных сил:", self.horse_powers())

print("Nissan")
my_car = Nissan()
my_car.inspect()
print("Kia")
my_car = Kia()
my_car.inspect()