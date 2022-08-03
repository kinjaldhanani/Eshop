
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post']
    queryset = Comment.objects.all()

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)
