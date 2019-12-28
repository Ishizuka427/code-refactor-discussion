import pytest
import calc


@pytest.mark.parametrize(
    ["test_input", "expected"], [([10, 5], (15, 5)), ([3, 10], (13, -7)),],
)
def test_calc(test_input, expected):
        print(*test_input)
        assert calc.calcadd(*test_input) == expected[0]
        assert calc.calcsub(*test_input) == expected[1]
