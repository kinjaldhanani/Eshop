
import factory
from factory.django import DjangoModelFactory

from category.factory import CategoryFactory
from product.models import Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("name")
    price = factory.Faker("random_int")
    description = factory.Faker("name")
    category = factory.SubFactory(CategoryFactory)
