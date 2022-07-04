from rest_framework import routers

from comment import views

app_name = 'comment'
router = routers.SimpleRouter()
router.register('comment', views.CommentView)

urlpatterns = [

    # path('signup/', SignUpView.as_view(), name='signup'),
]
urlpatterns += router.urls
