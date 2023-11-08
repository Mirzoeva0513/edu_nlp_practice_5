from typing import TYPE_CHECKING
from collections.abc import Iterable, Iterator
import pytest

if TYPE_CHECKING:
    import tests.stub as task_4  # type: ignore
else:
    import task_4


def test_primes_protocol():
    assert issubclass(
        task_4.Primes, Iterator
    ), "class Primes must implement method __next__"
    assert issubclass(
        task_4.Primes, Iterable
    ), "class Primes must implement method __iter__"


@pytest.mark.parametrize(
    "start, end, expected",
    [
        [1, 10, [2, 3, 5, 7]],
        [3, 3, []],
        [50, 100, [53, 59, 61, 67, 71, 73, 79, 83, 89, 97]],
    ],
)
def test_primes_contents(start: int, end: int, expected: list[int]):
    primes = task_4.Primes(start, end)
    assert list(primes) == expected
