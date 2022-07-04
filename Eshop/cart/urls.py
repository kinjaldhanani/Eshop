from rest_framework import routers

from cart import views

app_name = 'cart'

router = routers.SimpleRouter()
router.register('cart', views.CartView)
router.register('item', views.CartItemViewSet)

urlpatterns = [

    # path('signup/', SignUpView.as_view(), name='signup'),
    ]
urlpatterns += router.urls