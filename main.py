print("Programming", "Essential", "in")
print("Python")

print("    *    ")
print("   * *   ")
print("  *   *  ")
print(" *     * ")
print("***   *** ")
print("  *   * ")
print("  *   * ")
print("  ***** ")

print('"I am"\n""Learning""\n"""Python"""')

def octal_to_decimal(octal_str):
    decimal_num = 0
    power = 0

    # Переворачиваем строку с числом, чтобы начать с младших разрядов
    octal_str = octal_str[::-1]

    for digit in octal_str:
        # Переводим символ числа в целое число
        digit_value = int(digit)

        # Умножаем значение разряда на 8 в степени текущей позиции и добавляем к десятичному числу
        decimal_num += digit_value * (8 ** power)

        # Увеличиваем степень
        power += 1

    return decimal_num

# Ввод числа в восьмеричной системе
octal_number = input("Введите число в восьмеричной системе: ")

# Вызываем функцию и выводим результат
decimal_number = octal_to_decimal(octal_number)
print(f"Десятичное представление: {decimal_number}")

def hex_to_decimal(hex_str):
    decimal_num = 0

    # Переворачиваем строку с числом, чтобы начать с младших разрядов
    hex_str = hex_str[::-1]

    for i, digit in enumerate(hex_str):
        # Переводим символ числа в целое число
        if digit.isdigit():
            digit_value = int(digit)
        else:
            # Если символ - буква (A-F), то преобразуем его в соответствующее значение
            digit_value = ord(digit.upper()) - ord('A') + 10

        # Умножаем значение разряда на 16 в степени текущей позиции и добавляем к десятичному числу
        decimal_num += digit_value * (16 ** i)

    return decimal_num

# Ввод числа в шестнадцатеричной системе
hex_number = input("Введите число в шестнадцатеричной системе: ")

# Вызываем функцию и выводим результат
decimal_number = hex_to_decimal(hex_number)
print(f"Десятичное представление: {decimal_number}")