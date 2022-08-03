import pytest

from user_info.models import User


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


    }
    return USER_DATA


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

@pytest.fixture
def test_admin_user(db) -> User:
    admin = User.objects.create_superuser(username="admin",
                                          email="admin@trootech.com",
                                          password="admin@123###")
    return admin