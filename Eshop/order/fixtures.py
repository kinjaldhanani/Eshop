import pytest

from order.factory import OrderFactory
from order.models import Order


@pytest.fixture
def test_order_factory(db) -> Order:
    factory = OrderFactory.create()
    return factory