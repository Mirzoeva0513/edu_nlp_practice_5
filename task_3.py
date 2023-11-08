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
    def _recurrent(_s: str, acc: str):
        for i, ch in enumerate(_s):
            res = acc + ch
            if len(res) <= n:
                yield res
            _next_s = _s[:i] + _s[i + 1 :]
            yield from _recurrent(_next_s, res)

    return _recurrent(s, "")
    ### конец решения
