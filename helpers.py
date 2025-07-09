import random

from data import ingredients
from data import buns
from data import types

class HelpersMethods:

    @staticmethod
    def generate_random_price():
        random_price = round(random.uniform(0, 999), 2)
        return random_price

    @staticmethod
    def choose_random_ingredient():
        random_ingredient = random.choice(ingredients)
        return random_ingredient

    @staticmethod
    def choose_random_type():
        random_type = random.choice(types)
        return random_type

    @staticmethod
    def choose_random_bun_name():
        random_bun = random.choice(buns)
        return random_bun

    @staticmethod
    def choose_random_ingredient_name():
        random_ingredient = random.choice(ingredients)
        return random_ingredient