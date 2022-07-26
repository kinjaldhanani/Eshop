import uuid

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


@pytest.fixture
def test_login(db) -> User:
    LOGIN_DATA = {
        "username": "jinal",
        "password": "jinal@123#"
    }
    return LOGIN_DATA


def test_function(db, test_user,test_login):

    url = reverse("user_info:user-list")
    user_data = client.post(url, test_user, format='json')

    url1 = reverse("user_info:login")
    login_user_data = client.post(url1, test_login, format='json')

    assert user_data.status_code == status.HTTP_201_CREATED
    assert login_user_data.status_code == status.HTTP_200_OK


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user