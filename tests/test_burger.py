from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_bun_is_added_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun

    def test_add_ingredient_ingredient_is_added_success(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients

    def test_remove_ingredient_ingredient_is_removed_success(self, burger_with_ingredient):
        burger_with_ingredient.remove_ingredient(0)
        assert len(burger_with_ingredient.ingredients) == 0

    def test_move_ingredient_ingredient_is_moved_success(self, burger_with_ingredient, mock_ingredient):
        burger_with_ingredient.add_ingredient(mock_ingredient)
        first_ingredient = burger_with_ingredient.ingredients[0]
        second_ingredient = burger_with_ingredient.ingredients[1]
        burger_with_ingredient.move_ingredient(0, 1)
        assert burger_with_ingredient.ingredients[1] == first_ingredient and second_ingredient == burger_with_ingredient.ingredients[0]

    def test_get_price_get_burger_price_success(self, burger_with_bun_and_ingredient):
        burger, mock_bun, mock_ingredient = burger_with_bun_and_ingredient
        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    def test_get_receipt_get_burger_receipt_success(self, burger_with_bun_and_ingredient):
        burger, mock_bun, mock_ingredient = burger_with_bun_and_ingredient
        receipt = burger.get_receipt()
        assert (mock_bun.get_name() in receipt) and (mock_ingredient.get_type().lower() in receipt) and (mock_ingredient.get_name() in receipt) and (str(burger.get_price()) in receipt)











