import json

import pytest
from django.urls import reverse
from rest_framework import status
from user_info.models import User
from django.test import Client

from rest_framework.test import APIClient

client = APIClient()


def test_admin(db, test_admin_user):
    url1 = "http://127.0.0.1:8000/api/v1/login/"
    user_data = {
        "username": "admin",
        "password": "admin@123###"
    }
    responce = client.post(url1, user_data, format='json')
    assert responce.status_code == status.HTTP_200_OK


def test_register_with_valid_data(db, test_user):
    url = reverse("user_info:user-list")
    user_data = client.post(url, test_user, format='json')
    assert user_data.status_code == status.HTTP_201_CREATED


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


def test_change_password(db, test_admin_user):
    client.force_authenticate(test_admin_user)

    url1 = "http://127.0.0.1:8000/api/v1/change-password/"
    data = {
        'old_password': test_admin_user.password,
        'new_password': "admin",

    }
    test_password = client.patch(url1, data=data, format='json')
    assert test_password.status_code == status.HTTP_200_OK
