
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from Eshop.permission import IsOwner
from comment.models import Comment
from comment.serializer import CommentSerializer


class CommentView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)
