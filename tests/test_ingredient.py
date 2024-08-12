from ..praktikum.ingredient import Ingredient
from ..praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == "SAUCE"

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_price() == 100
