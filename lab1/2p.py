units = {
    "км": 1000,
    "м": 1,
    "см": 0.01,
    "мм": 0.001,
    "mi": 1609.344,
    "yd": 0.9144
}

print("Доступные единицы: км, м, см, мм, mi, yd")
source = input("Исходная единица: ").strip()
target = input("Целевая единица: ").strip()
value = float(input("Введите расстояние: "))

if source in units and target in units:
    result = value * units[source] / units[target]
    print(f"Результат: {result:.2f} {target}")
else:
    print("Ошибка: неизвестная единица измерения.")
