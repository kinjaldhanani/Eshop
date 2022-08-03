from factory.django import DjangoModelFactory
import factory

from comment.models import Comment


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    date = factory.Faker('date')
    comment = factory.Faker('name')
