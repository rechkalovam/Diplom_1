import pytest
from praktikum.bun import Bun
from data import buns
from helpers import HelpersMethods


class TestBun:

    @pytest.mark.parametrize('name', [buns[0], buns[1]])
    def test_get_name_return_bun_name_success(self, name):
        price = HelpersMethods.generate_random_price()
        bun = Bun(name, price)
        assert bun.name == name

    def test_get_price_return_bun_price_success(self):
        price = HelpersMethods.generate_random_price()
        name = HelpersMethods.choose_random_bun_name()
        bun = Bun(name, price)
        assert bun.price == price
