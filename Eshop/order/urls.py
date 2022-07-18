from rest_framework import routers

from order import views

app_name = 'order'

router = routers.SimpleRouter()
router.register('order', views.OrderView)



urlpatterns = [

    # path('signup/', SignUpView.as_view(), name='signup'),
    ]
urlpatterns += router.urls