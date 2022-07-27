import pytest
from rest_framework import status
from django.test import Client
from django.urls import reverse


client = Client()


@pytest.mark.django_db
def test_category_detail():
    CATEGORY_DATA = {
        "name": "Home1",
        "description": "description1",
        "subcategory": [
            {
                "name": "cook wear12",
                "description": "description123"
            }
        ]

    }
    url = reverse("category:category-list")
    category_data = client.post(url, data=CATEGORY_DATA, content_type="application/json")
    assert category_data.status_code == status.HTTP_201_CREATED

