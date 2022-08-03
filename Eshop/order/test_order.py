from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()


def test_order_create(db, test_admin_user, test_order_factory, test_product_factory):
    """ order create"""
    client.force_authenticate(test_admin_user)

    url = "http://127.0.0.1:8000/api/v1/order/"
    data = {
        "address": test_order_factory.address,
        "phone": test_order_factory.phone,
        "items": [
            {
                "product": test_product_factory.id,
                "quantity": "1"

            }

        ]
    }
    order_data = client.post(url, data=data, format="json")
    assert order_data.status_code == status.HTTP_201_CREATED


def test_order_get(db, test_admin_user, test_order_factory, test_product_factory):
    client.force_authenticate(test_admin_user)

    url1 = "http://127.0.0.1:8000/api/v1/order/"
    data = {
        "address": test_order_factory.address,
        "phone": test_order_factory.phone,
        "items": [
            {
                "product": test_product_factory.id,
                "quantity": "1"

            }
        ]
    }
    data = client.get(url1, data=data, format="json")
    assert data.status_code == status.HTTP_200_OK


