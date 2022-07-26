# import pytest
# from django.urls import reverse
# from rest_framework import status
# from django.test import Client
#
# client = Client()
#
#
# @pytest.mark.django_db
# def test_product():
#     """product testcases"""
#
#     PRODUCT_DATA = {
#         "name": "Home",
#         "price": "gugkjh",
#         "category": "321",
#         "description": "fgsfdhgshg",
#         "image": "",
#         "likes": "",
#     }
#     import pdb; pdb.set_trace()
#     url = reverse("product:product-list")
#     product_data = client.post(url, data=PRODUCT_DATA, content_type="application/json")
#     assert product_data.status_code == status.HTTP_201_CREATED
