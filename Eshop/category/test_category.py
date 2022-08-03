
from django.urls import reverse
from pytest_factoryboy import register
from rest_framework import status
from rest_framework.test import APIClient
from category.factory import CategoryFactory


client = APIClient()

register(CategoryFactory)


def test_category_create(db, test_admin_user, test_factory):
    """category create"""

    client.force_authenticate(test_admin_user)
    url = reverse("category:category-list")
    data = {
        "name": test_factory.name,
        "description": test_factory.description,
        "subcategory": [
            {
                "name": "cook wear",
                "description": "good"
            }
        ]
    }
    response = client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


def test_category_update(db, test_admin_user,test_factory):
    """category update"""

    client.force_authenticate(test_admin_user)
    url = "http://127.0.0.1:8000/api/v1/cat/{id}/".format(id=test_factory.id)
    data = {
        "name": "abc",
        "description": "abcdef",
        "subcategory": [
            {

                "name": "cook wear1",
                "description": "good1"
            }
        ]
    }
    category_data = client.patch(url, data=data, format="json")

    """Subcategory update"""

    client.force_authenticate(test_admin_user)

    url1 = "http://127.0.0.1:8000/api/v1/cat/{id}/".format(id=test_factory.id)
    id = category_data.json().get('subcategory')[0]['id']  # json data get in dict

    data = {
        "name": "abc",
        "description": "abcdef",
        "subcategory": [
            {
                "id": str(id),
                "name": "cook wear12345",
                "description": "good12345"
            }
        ]
    }
    subcategory_data = client.patch(url1, data=data, format="json")

    assert category_data.status_code == status.HTTP_200_OK
    assert subcategory_data.status_code == status.HTTP_200_OK


def test_category_delete(db, test_admin_user, test_factory):
    client.force_authenticate(test_admin_user)
    url = "http://127.0.0.1:8000/api/v1/cat/{id}/".format(id=test_factory.id)
    data = client.delete(url, format='json')
    assert data.status_code == status.HTTP_204_NO_CONTENT
