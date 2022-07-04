from django.urls import path
from rest_framework import routers
from user_info.views import ChangePasswordView, SignupView, LoginView
from knox.views import LogoutView, LogoutAllView

app_name = 'user_info'

router = routers.SimpleRouter()
router.register('signup', SignupView)

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', LogoutAllView.as_view(), name='knox_logoutall'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
urlpatterns += router.urls
