from rest_framework import status
from cart.factory import ItemFactory
from pytest_factoryboy import register
from rest_framework.test import APIClient

client = APIClient()
register(ItemFactory)


def test_cart_item_create(db, test_admin_user, test_product_factory, test_cart_item_factory):
    """cart item create"""
    client.force_authenticate(test_admin_user)

    url = "http://127.0.0.1:8000/api/v1/item/"
    data = {
        "product": test_product_factory.id,
        "quantity": test_cart_item_factory.quantity,
    }
    cart_item_data = client.post(url, data=data, format="json")
    assert cart_item_data.status_code == status.HTTP_201_CREATED


def test_cart_item_valid_update(db, test_admin_user, test_product_factory, test_cart_item_factory):
    client.force_authenticate(test_cart_item_factory.cart.customer)

    url = "http://127.0.0.1:8000/api/v1/item/{id}/".format(id=test_cart_item_factory.id)
    data = {
        "product": "2",
        "quantity": "11",

    }
    response = client.patch(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK


def test_cart_item_invalid_update(db, test_admin_user, test_product_factory, test_cart_item_factory):
    """You do not have permission to perform this action"""

    client.force_authenticate(test_admin_user)
    url = "http://127.0.0.1:8000/api/v1/item/{id}/".format(id=test_cart_item_factory.id)
    data = {

        "id": test_cart_item_factory.id,
        "product": test_product_factory.id,
        "quantity": "1"
    }

    data = client.patch(url, data=data, format="json")
    assert data.status_code == status.HTTP_403_FORBIDDEN


def test_cart_item_get(db, test_admin_user, test_product_factory):
    """cart item display"""
    client.force_authenticate(test_admin_user)

    url = "http://127.0.0.1:8000/api/v1/item/"
    data = {
        "product": test_product_factory.id,
        "quantity": "1",
    }
    cart_item_data = client.get(url, data=data, format="json")
    assert cart_item_data.status_code == status.HTTP_200_OK


def test_cart_item_delete(db, test_admin_user, test_cart_item_factory):
    client.force_authenticate(test_cart_item_factory.cart.customer)
    url = "http://127.0.0.1:8000/api/v1/item/{id}/".format(id=test_cart_item_factory.id)
    data = client.delete(url, format='json')
    assert data.status_code == status.HTTP_204_NO_CONTENT
