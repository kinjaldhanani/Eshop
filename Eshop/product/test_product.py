from django.db.migrations import serializer
from rest_framework import status, viewsets
from product.factory import ProductFactory
from pytest_factoryboy import register
from rest_framework.test import APIClient

client = APIClient()
register(ProductFactory)


def test_product_create(db, test_admin_user, test_product_factory, test_factory):
    """product testcases"""
    client.force_authenticate(test_admin_user)
    url = "http://127.0.0.1:8000/api/v1/product/"
    data = [
        {

            "name": test_product_factory.name,
            "price": test_product_factory.price,
            "category": test_factory.id,
            "description": test_product_factory.description
        }

    ]

    product_data = client.post(url, data=data, format='json')
    assert product_data.status_code == status.HTTP_201_CREATED


def test_product_update(db, test_factory, test_admin_user, test_product_factory):
    client.force_authenticate(test_admin_user)

    url = "http://127.0.0.1:8000/api/v1/product/{id}/".format(id=test_product_factory.id)
    data = [
        {
            "id": test_product_factory.id,
            "name": "kurta",
            "price": 2000,
            "category": test_factory.id,
            "description": "good!"
        },
        {
            "name": "kurti",
            "price": 1000,
            "category": test_factory.id,
            "description": "very good!"
        }
    ]

    product_data = client.patch(url, data=data, format='json')
    assert product_data.status_code == status.HTTP_200_OK


def test_product_delete(db, test_factory, test_admin_user, test_product_factory):
    client.force_authenticate(test_admin_user)
    url = "http://127.0.0.1:8000/api/v1/product/{id}/".format(id=test_product_factory.id)
    data = client.delete(url, format='json')
    assert data.status_code == status.HTTP_204_NO_CONTENT
