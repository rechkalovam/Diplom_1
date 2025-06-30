import pytest
from unittest.mock import Mock
from helpers import HelpersMethods
from praktikum.burger import Burger


@pytest.fixture()
def mock_bun():
    name = HelpersMethods.choose_random_bun_name()
    price = HelpersMethods.generate_random_price()
    mock_bun = Mock()
    mock_bun.name = name
    mock_bun.price = price
    mock_bun.get_price.return_value = price
    mock_bun.get_name.return_value = name
    return mock_bun

@pytest.fixture()
def mock_ingredient():
    name = HelpersMethods.choose_random_ingredient()
    price = HelpersMethods.generate_random_price()
    type = HelpersMethods.choose_random_type()
    mock_ingredient = Mock()
    mock_ingredient.name = name
    mock_ingredient.price = price
    mock_ingredient.type = type
    mock_ingredient.get_price.return_value = price
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_type.return_value = type
    return mock_ingredient

@pytest.fixture()
def burger_with_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    return burger

@pytest.fixture()
def burger_with_bun_and_ingredient(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger, mock_bun, mock_ingredient