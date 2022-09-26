import pytest


def increase(x):
    return x + 1


class TestIncreaseNumber:
    @pytest.mark.smoke
    @pytest.mark.increase
    def test_increase_zero(self):
        assert increase(0) == 1

    @pytest.mark.smoke
    @pytest.mark.increase
    def test_increase_positive_number(self):
        assert increase(1) == 2

    @pytest.mark.smoke
    @pytest.mark.increase
    def test_increase_negative(self):
        assert increase(-1) == 0

    @pytest.mark.smoke
    @pytest.mark.increase
    def test_increase_big_number(self):
        assert increase(999999999) == 1000000000

    @pytest.mark.smoke
    @pytest.mark.increase
    @pytest.mark.xfail(raises=TypeError, reason="illegal input")
    def test_increase_illegal_input(self):
        assert increase('x') == "x1"
