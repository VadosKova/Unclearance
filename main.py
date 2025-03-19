# class Car:
#     def __init__(self, id, name, type_of_engine, volume_of_engine, type_of_fuel, creation_year, country, action_bet):
#         self.id = id
#         self.name = name
#         self.type_of_engine = type_of_engine
#         self.volume_of_engine = volume_of_engine  # Объем двигателя (л) или мощность (кВт)
#         self.type_of_fuel = type_of_fuel
#         self.creation_year = creation_year
#         self.country = country  # Можно удалить, если не требуется
#         self.action_bet = action_bet  # Акцизная ставка
#

class CustomsCalculator:
    def __init__(self, car: Car):
        self.car = car

    def calculate_duty(self):
        base_duty = 1000
        age = 2025 - self.car.creation_year
        volume_factor = self.car.volume_of_engine * 50
        age_factor = age * 100
        tax = base_duty + volume_factor + age_factor
        return tax

    def calculate_vat(self):
        vat_rate = 0.2
        vat = self.calculate_duty() * vat_rate
        return vat

    def calculate_total_customs_fee(self):
        return self.calculate_duty() + self.calculate_vat()

