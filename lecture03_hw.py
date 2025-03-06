def convert_temperature(temp_str):
    # Проверяем наличие буквы 'C' или 'F'
    if temp_str.endswith('C'):        #перевод из градусов в фаренгейты
        celsius = float(temp_str[:-1])
        fahrenheit = celsius * 9 / 5 + 32
        return f"{fahrenheit:.2f}F" #два знака после запятой и фаренгейт
    elif temp_str.endswith('F'):
        fahrenheit = float(temp_str[:-1])
        celsius = (fahrenheit - 32) * 5 / 9
        return f"{celsius:.2f}C"
    else:
        return "Неверный формат ввода. Пожалуйста, введите температуру в формате NC или NF."

# Основная программа
user_input = input("Введите температуру в градусах Цельсия или Фаренгейта (например, 12C или 100F): ")

result = convert_temperature(user_input)
print(f"Ваш результат: {result}")