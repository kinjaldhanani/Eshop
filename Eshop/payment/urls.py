from rest_framework import routers

from payment import views

app_name = 'payment'

router = routers.SimpleRouter()
router.register('payment', views.PaymentView)


urlpatterns = [
    ]
urlpatterns += router.urls