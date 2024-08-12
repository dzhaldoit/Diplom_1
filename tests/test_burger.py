from ..praktikum.burger import Burger
from ..praktikum.bun import Bun
from ..praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_bun(self):

        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):

        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)

        ingredient = Ingredient("sauce", "hot sauce", 100)
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):

        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)

        ingredient = Ingredient("sauce","hot sauce", 100)
        burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)

        ingredient = Ingredient("sauce", "hot sauce", 100)
        ingredient2 = Ingredient("sauce", "sour cream", 200)

        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)

        assert ingredient in burger.ingredients
        assert ingredient2 in burger.ingredients

    def test_get_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)

        ingredient = Ingredient("sauce", "hot sauce", 100)
        ingredient2 = Ingredient("sauce", "sour cream", 200)

        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)

        assert burger.get_price() == 500

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)

        ingredient = Ingredient("sauce", "hot sauce", 100)
        ingredient2 = Ingredient("sauce", "sour cream", 200)

        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)

        expected_receipt = (f"(==== {bun.get_name()} ====)\n= sauce hot sauce ="
                            f"\n= sauce sour cream =\n(==== {bun.get_name()} ====)\n\nPrice: {burger.get_price()}")
        assert burger.get_receipt() == expected_receipt
