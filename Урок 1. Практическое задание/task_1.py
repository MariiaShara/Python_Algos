"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""
NUM = int(input("Введите целое трехзначное число: "))
SUM = (NUM // 100) + ((NUM // 10) % 10) + (NUM % 10)
PROD = (NUM // 100) * ((NUM // 10) % 10) *  (NUM % 10)
print(f"Сумма цифр числа = {SUM} ")
print(f"Произведение цифр числа = {PROD}")
