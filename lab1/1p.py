import math

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника: {s:.2f}")
else:
    print("Треугольник с такими сторонами не существует.")
