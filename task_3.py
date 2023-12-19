"""
Реализовать функцию get_combinations, принимающую строку s и число k и
генерирующую все сочетания длины n <= k символов строки s. Сочетания должны быть
представлены строками (тип str). Порядок генерации сочетаний может быть
произвольным.

Пример использования функции get_combinations:

s = "cat"
n = 2

for c in get_combinations(s, n):
    print(c)

# a
# c
# t
# ac
# at
# ct

В Python похожий функционал реализован в пакете itertools функцией combinations.
В рамках этой работы пользоваться пакетом itertools запрещено!


В комбинаторике сочетанием длины k конечного множества A называется набор из k
элементов, выбранных из множества A, в котором не учитывается порядок элементов.
https://ru.wikipedia.org/wiki/Сочетание

Для множества A = [1,2,3,4] существуют следующие сочетания длины 2: (1,2),
(1,3), (1,4), (2,3), (2,4), (3,4)
"""


def get_combinations(s: str, n: int):
    ### начало решения
   def get_combinations(s, n):
    if n == 0 or len(s) == 0:
        return []
    elif n == 1:
        return list(s)
    else:
        combinations = []
        for i in range(len(s)):
            combinations.append(s[i])
            partials = get_combinations(s[i+1:], n-1)
            for partial in partials:
                combinations.append(s[i] + partial)
                combinations.append(partial + s[i])
        if n > 2:
            combinations = list(set([perm for c in combinations for perm in get_permutations(c)]))
        return combinations

def get_permutations(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            rest = s[:i] + s[i+1:]
            for p in get_permutations(rest):
                perms.append(s[i] + p)
        return perms
    ### конец решения
