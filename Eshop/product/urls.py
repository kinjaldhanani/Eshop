from rest_framework import routers

from product import views

app_name = 'product'

router = routers.SimpleRouter()
router.register('home',views.HomeView)
router.register('product',views.ProductView)

urlpatterns = [

    # path('signup/', SignUpView.as_view(), name='signup'),
    ]
urlpatterns += router.urls