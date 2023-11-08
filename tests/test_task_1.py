from typing import TYPE_CHECKING
import pytest

if TYPE_CHECKING:
    import tests.stub as task_1  # type: ignore
else:
    import task_1


@pytest.mark.parametrize(
    "a, b, expected",
    [
        [
            [1, 2],
            [3, 4],
            [(1, 3), (1, 4), (2, 3), (2, 4)],
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)],
        ],
    ],
)
def test_cartesian_product(
    a: list[int],
    b: list[int],
    expected: list[tuple[int, ...]],
):
    actual = task_1.get_cartesian_product(a, b)
    assert set(actual) == set(expected)
