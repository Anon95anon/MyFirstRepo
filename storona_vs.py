#Вам необходимо написать программу, которая находит длину третьей стороны произвольного треугольника по двум его сторонам и углу между ними. Можно использовать для этого теорему косинусов

import math 
def calculate_third_side(a, b, degrees):
  """
  Вычисляет длину третьей стороны треугольника по теореме косинусов.

  Args:
    a: Длина стороны a.
    b: Длина стороны b.
    degrees: Угол между сторонами a и b в градусах.

  Returns:
    Длина третьей стороны c.
  """
  angle_radians = math.radians(degrees)  # Преобразуем градусы в радианы
  side_c_squared = a**2 + b**2 - 2 * a * b * math.cos(angle_radians)
  c = math.sqrt(side_c_squared)
  return c

# Пример использования
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
degrees = float(input("Введите угол между сторонами a и b в градусах: "))

c = calculate_third_side(a, b, degrees)

print("Длина третьей стороны c:", c)

