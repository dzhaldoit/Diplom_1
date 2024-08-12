import pytest
from ..praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price', [("red_bun", 100),
                                             ("white bun", 200),
                                             ("black bun", 300)
                                             ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [("red_bun", 100),
                                             ("white bun", 200),
                                             ("black bun", 300)
                                             ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    def test_price_type(self):
        bun = Bun("black bun", 10.0)
        assert type(bun.get_price()) == float

