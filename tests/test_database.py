from praktikum.database import Database
from data import available_buns
from data import available_ingredients


class TestDatabase:

    def test_available_buns_get_buns_success(self):
         database = Database()
         assert [{"name": bun.name, "price": bun.price} for bun in database.available_buns()] == available_buns

    def test_available_ingredients_get_ingredients_success(self):
        database = Database()
        assert [{"type": ing.type, "name": ing.name, "price": ing.price} for ing in database.available_ingredients()] == available_ingredients