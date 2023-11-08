from __future__ import annotations

from collections.abc import Generator
from typing_extensions import Self

# task 1

def get_cartesian_product(
    a: list[int], b: list[int]
) -> Generator[tuple[int, ...], None, None]: ...

# task 2

def get_permutations(s: str, n: int) -> Generator[str, None, None]: ...

# task 3

def get_combinations(s: str, n: int) -> Generator[str, None, None]: ...

# task 4

class Primes:
    def __init__(self, start: int, end: int) -> None: ...
    def __next__(self) -> int: ...
    def __iter__(self) -> Self: ...
    def __add__(self, other) -> Self: ...
