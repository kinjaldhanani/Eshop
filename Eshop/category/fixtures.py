import pytest

from category.models import Category
from category.factory import CategoryFactory



@pytest.fixture
def test_factory(db) -> Category:
    factory = CategoryFactory.create()
    return factory



