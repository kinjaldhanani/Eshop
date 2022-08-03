from rest_framework import routers

from cart import views

app_name = 'cart'

router = routers.SimpleRouter()
router.register('item', views.CartItemView)

urlpatterns = [

    # path('signup/', SignUpView.as_view(), name='signup'),
    ]
urlpatterns += router.urls