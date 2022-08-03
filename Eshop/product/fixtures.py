import pytest

from product.factory import ProductFactory
from product.models import Product


@pytest.fixture
def test_product_factory(db) -> Product:
    factory = ProductFactory.create()
    return factory

