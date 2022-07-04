from rest_framework import routers

from category import views

app_name = 'category'

router = routers.SimpleRouter()
router.register('cat', views.CategoryView)
urlpatterns = [

    # path('signup/', SignUpView.as_view(), name='signup'),
    ]
urlpatterns += router.urls
