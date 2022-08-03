import factory
from factory.django import DjangoModelFactory

from category.models import Category


class ParentFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    description = factory.Faker("name")


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    description = factory.Faker("name")
    parent = factory.SubFactory(ParentFactory)
