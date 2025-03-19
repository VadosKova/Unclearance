import tkinter as tk
from tkinter import messagebox

class Car:
    def __init__(self, id, name, type_of_engine, volume_of_engine, type_of_fuel, creation_year, country, action_bet):
        self.id = id
        self.name = name
        self.type_of_engine = type_of_engine
        self.volume_of_engine = volume_of_engine
        self.type_of_fuel = type_of_fuel
        self.creation_year = creation_year
        self.country = country
        self.action_bet = action_bet

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

def calculate():
    try:
        car = Car(
            id=1,
            name=entry_name.get(),
            type_of_engine=entry_engine.get(),
            volume_of_engine=float(entry_volume.get()),
            type_of_fuel=entry_fuel.get(),
            creation_year=int(entry_year.get()),
            country=entry_country.get(),
            action_bet=0
        )
        calculator = CustomsCalculator(car)
        duty = calculator.calculate_duty()
        vat = calculator.calculate_vat()
        total = calculator.calculate_total_customs_fee()
        messagebox.showinfo("Результат", f"Акциз: {duty}\nНДС: {vat}\nИтого: {total}")
    except ValueError:
        messagebox.showerror("Ошибка", "Проверьте правильность введенных данных!")

root = tk.Tk()
root.title("Калькулятор таможенных платежей")
root.geometry("250x250")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(expand=True)

labels = ["Название", "Тип двигателя", "Объем двигателя", "Тип топлива", "Год выпуска", "Страна"]
entries = []
for i, label in enumerate(labels):
    tk.Label(frame, text=label).grid(row=i, column=0, pady=2, padx=5, sticky="e")
    entry = tk.Entry(frame)
    entry.grid(row=i, column=1, pady=2, padx=5)
    entries.append(entry)

entry_name, entry_engine, entry_volume, entry_fuel, entry_year, entry_country = entries

tk.Button(frame, text="Рассчитать", command=calculate).grid(row=len(labels), column=0, columnspan=2, pady=10)
root.mainloop()