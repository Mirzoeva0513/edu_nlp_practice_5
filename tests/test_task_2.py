from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
    import tests.stub as task_2  # type: ignore
else:
    import task_2


@pytest.mark.parametrize(
    "text, n, expected",
    [
        ["cat", 2, ["ac", "at", "ca", "ct", "ta", "tc"]],
        # fmt: off
        ["abcd", 3, ["abc", "abd", "acb", "acd", "adb", "adc", "bac", "bad", "bca", "bcd", "bda", "bdc", "cab", "cad", "cba", "cbd", "cda", "cdb", "dab", "dac", "dba", "dbc", "dca", "dcb"]],
        # fmt: on
    ],
)
def test_permutations(text: str, n: int, expected: list[str]):
    actual = task_2.get_permutations(text, n)
    assert set(actual) == set(expected)
