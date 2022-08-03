import pytest

from cart.factory import ItemFactory
from cart.models import Item

@pytest.fixture
def test_cart_item_factory(db) -> Item:
    factory = ItemFactory.create()
    return factory


