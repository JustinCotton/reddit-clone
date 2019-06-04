from .views import PostViewSet, CommentViewSet, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('comments', CommentViewSet)

urlpatterns = router.urls