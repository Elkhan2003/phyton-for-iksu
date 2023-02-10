# ! 1
# print(31, 18, 79, sep=', ')

# ! 2
# print(round(3.1415926,2), '   ', round(2.71828, 2))

# ! 3
# a = int(input('Введите значение переменной: '))
# y = 3*a**2 + 5*a - 21
# print('Значение функции y равно:', y)

# ! 4
# petya_and_sereja = int(input('Сколько журавликов сделали Петя и Сережа вместе? '))
# kate = petya_and_sereja * 2
# print('Катя сделала', kate, 'журавликов')

# ! 5
# percent = 100 * (n - x) / n
# print(percent)

# ! 6
# N = int(input("Введите количество панелей: "))
# A = int(input("Введите длину панели в метрах: "))
# B = int(input("Введите ширину панели в метрах: "))

# needed_sulfite = 3 * N * A * B

# print("Необходимое количество сульфита:", needed_sulfite, "куб.м.")

# ! 7
# seconds = int(input("Введите количество секунд: "))
# minutes = seconds // 60
# rest_seconds = seconds % 60
# print(f"{minutes} минут и {rest_seconds} секунд")

# ! 8
# hours1 = int(input("Введите час первого момента: "))
# minutes1 = int(input("Введите минуту первого момента: "))
# seconds1 = int(input("Введите секунду первого момента: "))

# hours2 = int(input("Введите час второго момента: "))
# minutes2 = int(input("Введите минуту второго момента: "))
# seconds2 = int(input("Введите секунду второго момента: "))

# delta_hours = hours2 - hours1
# delta_minutes = minutes2 - minutes1
# delta_seconds = seconds2 - seconds1

# delta_seconds_total = delta_hours * 3600 + delta_minutes * 60 + delta_seconds

# print(f"Между двумя моментами прошло {delta_seconds_total} секунд")

# ! 9
import math

a = float(input("Введите значение а: "))

result = a + 5 / math.sqrt(a + 1)

print(result)

# ! 10
# num = int(input('Введите трехзначное целое число: '))

# # Получаем первую и последнюю цифру числа
# first_digit = num // 100
# last_digit = num % 10

# # Получаем новое число меняя местами первую и последнюю цифру
# new_num = last_digit * 100 + (num % 100 - last_digit) + first_digit

# print(f'Новое число: {new_num}')