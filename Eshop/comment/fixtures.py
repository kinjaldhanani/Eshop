import pytest

from comment.fectory import CommentFactory
from comment.models import Comment
from order.models import Order


@pytest.fixture
def test_comment_factory(db) -> Comment:
    factory = CommentFactory.create()
    return factory

