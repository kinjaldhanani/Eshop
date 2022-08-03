import factory
from factory.django import DjangoModelFactory

from cart.models import Cart, Item
from product.factory import ProductFactory
from user_info.models import User


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    city = factory.Faker("name")
    country = factory.Faker("name")
    Address = factory.Faker("name")


class CartFactory(DjangoModelFactory):
    class Meta:
        model = Cart

    date = factory.Faker("date")
    status = factory.Faker("boolean")
    customer = factory.SubFactory(CustomerFactory)


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item

    quantity = factory.Faker("random_int")
    cart = factory.SubFactory(CartFactory)
    product = factory.SubFactory(ProductFactory)
