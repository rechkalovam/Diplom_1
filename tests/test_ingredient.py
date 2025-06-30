import pytest
from data import ingredients
from praktikum.ingredient import Ingredient
from helpers import HelpersMethods
from data import types


class TestIngredient:

    @pytest.mark.parametrize('name', [ingredients[0], ingredients[1], ingredients[2], ingredients[3], ingredients[4], ingredients[5], ingredients[6], ingredients[7], ingredients[8], ingredients[9], ingredients[10]])
    def test_get_name_return_ingredient_name_success(self, name):
        type = HelpersMethods.choose_random_type()
        price = HelpersMethods.generate_random_price()
        ingredient = Ingredient(type, name, price)
        assert ingredient.name == name

    def test_get_price_return_ingredient_price_success(self):
        price = HelpersMethods.generate_random_price()
        name = HelpersMethods.choose_random_bun_name()
        type = HelpersMethods.choose_random_type()
        ingredient = Ingredient(type, name, price)
        assert ingredient.price == price

    @pytest.mark.parametrize('type', [types[0], types[1]])
    def test_get_type_return_ingredient_type_success(self, type):
        name = HelpersMethods.choose_random_ingredient_name()
        price = HelpersMethods.generate_random_price()
        ingredient = Ingredient(type, name, price)
        assert ingredient.type == type