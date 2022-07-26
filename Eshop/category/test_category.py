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

#
##############################
# import pytest
# from rest_framework import status
# from django.test import Client
# from django.urls import reverse
#
# from category.models import Category
# from user_info.models import User
#
# client = Client()
#
#
# @pytest.fixture
# def test_user(db) -> User:
#     USER_DATA = {
#         "username": "jinal",
#         "first_name": "jinal",
#         "last_name": "patel",
#         "email": "jinal.patel@trootech.com",
#         "password": "jinal@123#",
#         "Address": "abc",
#         "city": "Surat",
#         "country": "india",
#         "phone_number": "7894561230",
#         "gender": "f",
#         "birthdate": "14/05/1994",
#         "profile_image": "",
#
#     }
#     return USER_DATA
#
# @pytest.fixture
# def test_category(db)->Category:
#     CATEGORY_DATA = {
#         "name": "Home1",
#         "description": "description1",
#         "subcategory": [
#             {
#                 "name": "cook wear12",
#                 "description": "description123"
#             }
#         ]
#
#     }
#     return CATEGORY_DATA
# def test_category_detail(db, test_user,test_category):
#
#     import pdb; pdb.set_trace()
#     url1 = reverse("user_info:user-list")
#     user_data = client.post(url1, test_user, format='json')
#
#     url = reverse("category:category-list")
#     category_data = client.post(url, data=test_category, content_type="application/json")
#
#     assert user_data.status_code == status.HTTP_201_CREATED
#     assert category_data.status_code == status.HTTP_200_OK
