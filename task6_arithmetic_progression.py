# Задача 6: Арифметическая прогрессия
# Напишите программу, которая вычисляет n-ое число в арифметической прогрессии. Пользователь вводит первое число, шаг прогрессии и номер n.
# Пример:
# Ввод: Первое число: 2, Шаг: 3, n: 4
# Вывод: Результат: 11
n_1 = int(input('Первое число: '))
st = int(input('Шаг: '))
n = int(input('n: '))
n_n = n_1 + st * (n-1)
print('Результат:', n_n)
