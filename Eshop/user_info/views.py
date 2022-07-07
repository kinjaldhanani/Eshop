
from django.contrib.auth import login
from rest_framework import permissions, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from user_info.models import User
from user_info.serializers import ChangePasswordSerializer, SignUpSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated


class SignupView(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignUpSerializer
    queryset = User.objects.all()


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    # def update(self, request, *args, **kwargs):
    #     user = self.get_object()
    #     serializer = self.get_serializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         # Check old password
    #         if user.check_password(serializer.data.get("old_password")):
    #             return Response(
    #                 {"old_password": ["Wrong password."]},
    #                 status=status.HTTP_400_BAD_REQUEST,
    #             )
    #         # set_password also hashes the password that the user will get
    #         self.object.set_password(serializer.data.get("new_password"))
    #         self.object.save()
    #         response = {
    #             "status": "success",
    #             "code": status.HTTP_200_OK,
    #             "message": "Password updated successfully",
    #             "data": [],
    #         }
    #
    #         return Response(response)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
