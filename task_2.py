"""
Реализовать функцию get_permutations, принимающую строку s и число n и
генерирующую все перестановки длины n символов cтроки s. Перестановки должны
быть представлены строками (тип str). Порядок генерации перестановок может быть
произвольным.

Пример использования функции get_permutations:

s = "cat"
n = 2

for p in get_permutations(s, n):
    print(p)

# "ca"
# "ct"
# "ac"
# "at"
# "ta"
# "tc"

В Python похожий функционал реализован в пакете itertools функцией permutations.
В рамках этой работы пользоваться пакетом itertools запрещено!


В комбинаторике перестановкой длины N конечного множества X называется
произвольный упорядоченный набор из N элементов X (без повторений).
https://ru.wikipedia.org/wiki/Перестановка

Для множества A = [1, 2, 3] существуют следующие перестановки:
- длины 1: {1}, {2}, {3}
- длины 2: {1,2}, {1,3}, {2,1}, {2,3}, {3,1}, {3,2}
- длины 3: {1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}

def get_permutations (s, n):
    if n == 0 or len(s) == 0:
        return []
    elif n == 1:
        return list(s)
    else:
        permutations = []
        for i in range(len(s)):
            partials = get_permutations(s[:i] + s[i+1:], n-1)
            for partial in partials:
                permutations.append(s[i] + partial)
        return permutations

"""


def get_permutations(s, n):
    ### начало решения

    ### конец решения
