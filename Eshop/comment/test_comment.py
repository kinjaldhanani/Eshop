from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()


def test_comment_create(db, test_admin_user, test_comment_factory, test_product_factory):
    """ order create"""
    client.force_authenticate(test_admin_user)

    url = "http://127.0.0.1:8000/api/v1/comment/"
    data = {
        "product":test_product_factory.id,
        "comment":test_comment_factory.comment,
        "date": test_comment_factory.date
    }
    order_data = client.post(url, data=data, format="json")
    assert order_data.status_code == status.HTTP_201_CREATED


def test_comment_get(db, test_comment_factory,test_admin_user, test_product_factory):
    """ order create"""

    client.force_authenticate(test_admin_user)

    url = "http://127.0.0.1:8000/api/v1/comment/"
    data = {
        "product":test_product_factory.id,
        "comment":test_comment_factory.comment,
        "date": test_comment_factory.date
    }
    order_data = client.get(url, data=data, format="json")
    assert order_data.status_code == status.HTTP_200_OK