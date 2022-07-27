import json

import pytest
from django.urls import reverse
from rest_framework import status
from user_info.models import User
from django.test import Client

client = Client()


@pytest.fixture
def test_user(db) -> User:
    USER_DATA = {
        "username": "jinal",
        "first_name": "jinal",
        "last_name": "patel",
        "email": "jinal.patel@trootech.com",
        "password": "jinal@123#",
        "Address": "abc",
        "city": "Surat",
        "country": "india",
        "phone_number": "7894561230",
        "gender": "f",
        "birthdate": "14/05/1994",
        "profile_image": "",

    }
    return USER_DATA


def test_register_with_valid_data(db, test_user):
    url = reverse("user_info:user-list")
    user_data = client.post(url, test_user, format='json')
    assert user_data.status_code == status.HTTP_201_CREATED


@pytest.fixture
def test_user_invalid(db) -> User:
    USER_DATA = {
        "username": "jinal12",
        "first_name": "jinal12",
        "last_name": "patel",
        "email": "jinal.patel@trootech.com",
        "password": "jinal@123#",
        "Address": "abc",
        "city": "Surat",
        "country": "india",
        "phone_number": "7894561230",
        "gender": "f",
        "birthdate": "14/05/1994",
        "profile_image": "",

    }
    return USER_DATA


def test_register_with_invalid_exists(db, test_user, test_user_invalid):

    url = reverse("user_info:user-list")
    user_data = client.post(url, test_user, format='json')
    data = json.loads(user_data.content)
    test_user_create = client.post(url, test_user_invalid, format='json')
    assert test_user_create.status_code == status.HTTP_400_BAD_REQUEST



class Test:

    def setup(self):
        user = User.objects.create_user(username="admin1234566",
                                        email="admin1234@trootech.com",
                                        password="admin@123#")

        return user

    @pytest.mark.django_db
    def test_login_with_valid_data(self, db):
        url1 = reverse("user_info:login")
        data = {
            'username': "admin1234566",
            'email': "admin1234@trootech.com",
            'password': "admin@123#"

        }
        login_user = client.post(url1, data=data, format='json', )
        assert login_user.status_code == status.HTTP_200_OK
