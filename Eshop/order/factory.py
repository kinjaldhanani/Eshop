from factory.django import DjangoModelFactory
import factory
from order.models import Order


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    address = factory.Faker("name")
    phone = factory.Faker("random_int")
    date = factory.Faker('date')

