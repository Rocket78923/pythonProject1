#2
john = 3;
mary = 5;
adam = 6;
totalApple = 0;
print("john =", john,",","mary =", mary,",","adam =", adam)
totalApple = john+mary+adam;
print("Загальна кількість яблук =", totalApple);
#3
kilometers = 12.25
miles = 7.38
miles_to_kilometers = 1.60934
kilometers_to_miles = 0.621371
print(miles, "miles is", round(miles * miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers * kilometers_to_miles, 2), "miles")
#4
x =  0;
##x = int(input());
x = float(x);
y = 3 * pow(x, 3) - 2 * pow(x,2) + pow(3,x);
print("y =", y);
#5
# Calculate the number of seconds in a given number of hours
hours = 2  # Number of hours
seconds_per_hour = 3600  # Number of seconds in one hour
print("Hours: ", hours)  # Output the number of hours
# print("Seconds in Hours: ", hours * seconds_per_hour)  # Output the number of seconds in the given number of hours
#6
a = int(input())
b = int(input())
s = a + b
t = a - b
d = a / b
m = a * b
print(a, "+", b, "=", s)
print(a, "-", b, "=", t)
print(a, "/", b, "=", d)
print(a, "*", b, "=", m)
#7
#x = float(input("Enter value for x: "))
x = 1
y = 1/(x + 1 / (x + 1 / x + 1 / x + 1) / x);
print("y =", y)
#8
# Введення початкового часу (години і хвилини)
start_hour = int(input("Введіть години початку (0-23): "))
start_minute = int(input("Введіть хвилини початку (0-59): "))
# Введення тривалості в хвилинах
duration_minutes = int(input("Введіть тривалість події в хвилинах: "))
# Обчислення годин та хвилин закінчення
end_hour = (start_hour + (start_minute + duration_minutes) // 60) % 24
end_minute = (start_minute + duration_minutes) % 60
# Виведення результату
print(f"Подія закінчиться о {end_hour}:{end_minute}")