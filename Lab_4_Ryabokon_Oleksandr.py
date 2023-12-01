#1
n = int(input("Enter value for n: "))
result = n >= 100; print(result)
#2
fn = int(input("Enter value for fn: "))
sn = int(input("Enter value for sn: "))
if fn>sn:
    print("Число ", fn ,"більше за число", sn)
else : print("Число ", sn ,"більше за число", fn)
#3
# Введення рядка в нижньому регістрі
user_input = input("Введіть рядок: ")

# Переведення введення в верхній регістр для порівняння
user_input_upper = user_input.upper()

# Перевірка умов і вивід відповідного повідомлення
if user_input_upper == "SPATHIPHYLLUM":
    print("Yes - Spathiphyllum is the best plant ever!")
elif user_input_upper == "SPATHIPHYLLUM!":
    print(f"Spathiphyllum! Not {user_input}!")
else:
    print(f"No, I want a big Spathiphyllum!")
#4
# Ввід доходу від користувача
income = float(input("Введіть ваш дохід: "))

# Перевірка умов і розрахунок податку
if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02

# Заокруглення податку до цілих талерів
rounded_tax = round(tax)

# Виведення розрахованого податку
print("Розрахований податок: ", rounded_tax, "талерів")
#5
ny = int(input("Enter year: "))
if ny % 4 == 0 :
    print(ny ,"Common year")
else:
    print(ny ,"Leap year")
if ny < 1582 :
    print("Not within the Gregorian calendar period")
#6
secret_number = 7  # Секретне число обране фокусником

while True:
    user_input = input("Введіть ціле число (або q для виходу): ")

    if user_input == 'q':
        print("Гра завершена. До побачення!")
        break  # Виходимо з гри, якщо користувач ввів 'q'

    try:
        user_number = int(user_input)  # Спробуємо перетворити введення користувача в ціле число

        if user_number == secret_number:
            print("Молодець, магле! Тепер ти вільний.")
            break  # Виходимо з гри, якщо користувач вгадав число
        else:
            print("Ха-ха! Ви застрягли у моїй петлі!")
    except ValueError:
        print("Будь ласка, введіть ціле число або 'q' для виходу.")
#7
#8
word = input("Введіть слово: ")

while word != "chupacabra":
  print("Будь ласка, введіть ціле число або 'q' для виходу.")
  if word == "chupacabra": print("You've successfully left the loop")
#9
user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
#10
user_word = input("Введіть слово: ")
user_word = user_word.upper()
word_without_vowels = ''

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)
#12
def collatz_conjecture(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
        print(n)

    return steps


# Зчитуємо введене користувачем число
user_input = int(input("Введіть натуральне число: "))

# Виклик функції та виведення проміжних значень та кількості кроків
print("Проміжні значення:")
steps_taken = collatz_conjecture(user_input)
print(f"Кількість кроків: {steps_taken}")








