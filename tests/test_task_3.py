from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
    import tests.stub as task_3  # type: ignore
else:
    import task_3


@pytest.mark.parametrize(
    "text, k, expected",
    [
        ["cat", 2, ["a", "c", "t", "ac", "at", "ct", "ca", "ta", "tc"]],
        # fmt: off
        ["bar", 3, ["b", "a", "r", "ba", "br", "ab", "ar", "rb", "ra", "bar", "bra", "abr", "arb", "rba", "rab"]],
        # fmt: on
    ],
)
def test_combinations(text: str, k: int, expected: list[str]):
    actual = task_3.get_combinations(text, k)
    assert set(actual) == set(expected)
