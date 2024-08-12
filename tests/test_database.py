from ..praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()

        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"
        assert len(buns) == 3

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"
        assert len(ingredients) == 6
