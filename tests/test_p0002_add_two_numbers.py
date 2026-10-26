import pytest
from hypothesis import given, strategies as st

from solutions.p0002_add_two_numbers import Solution, build_linked_list, linked_list_to_list


@pytest.mark.parametrize(
    ('l1_values', 'l2_values', 'expected'),
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_add_two_numbers(l1_values: list[int], l2_values: list[int], expected: list[int]) -> None:
    l1 = build_linked_list(l1_values)
    l2 = build_linked_list(l2_values)

    result = Solution().addTwoNumbers(l1, l2)

    assert linked_list_to_list(result) == expected


@given(
    a=st.integers(min_value=0, max_value=10**50),
    b=st.integers(min_value=0, max_value=10**50),
)
def test_add_two_numbers_properties(a: int, b: int) -> None:
    l1 = build_linked_list([int(digit) for digit in str(a)[::-1]])
    l2 = build_linked_list([int(digit) for digit in str(b)[::-1]])

    result = Solution().addTwoNumbers(l1, l2)

    result_digits = linked_list_to_list(result)

    actual = sum(digit * 10**i for i, digit in enumerate(result_digits))

    assert actual == a + b
