"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import math
import timeit

# Вариант без использования «Решета Эратосфена»
def prime_num(i):
    l = 2
    m = 1000000
    my_set = set(range(2, m))
    for j in range(2, int(math.sqrt(m))):
        if j in my_set:
            my_set -= set(range(2*j, m, j))
    primes = sorted(list(my_set))
    return primes[i-1]


# Вариант с использованием «Решета Эратосфена»
def prime_num_erat(i):

    l = 2
    m = 1000000
    list = [i for i in range(m)]
    list[1] = 0
    n = 2
    while n < m:
        if list[n] != 0:
            p = n * 2
            while p < m:
                list[p] = 0
                p += n
        n += 1
    primes = [list[i] for i in list if list[i] != 0]
    del list
    return primes[i-1]

i = int(input('Введите порядковый номер искомого простого числа: '))
print(timeit.timeit("prime_num(i)", setup="from __main__ import prime_num, i", number=100))
print(timeit.timeit("prime_num_erat(i)", setup="from __main__ import prime_num_erat, i", number=100))


"""Результаты:
Время работы алгоритмов для поиска 10-го простого числа 100 раз:
простой - 0.1842969000000001
решето - 0.42815819999999993

Время работы алгоритмов для поиска 100-го простого числа 100 раз:
простой - 0.18078320000000003
решето - 0.41527840000000005

Время работы алгоритмов для поиска 1000-го простого числа 100 раз:
простой - 0.1898819000000005
решето - 0.40762880000000035

Время работы алгоритмов для поиска 10000-го простого числа 100 раз:
простой - 22.731788
решето - 58.150434800000006

В моем случае решето оказалось всегда медленнее."""

